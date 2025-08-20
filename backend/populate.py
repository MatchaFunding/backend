import os
import pandas as pd
import json
import re
import requests

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
DIR_POST = os.path.join(BASE_DIR, "data", "postulantes.csv")
DIR_PROY = os.path.join(BASE_DIR, "data", "proyectos.csv")
DIR_RELA = os.path.join(BASE_DIR, "data", "relaciones.csv")
MODEL = "deepseek-r1:8b"
API = "http://localhost:11434/api/generate"

CAMPOS_POSTULANTE = [
    "Nombre", "Creacion", "Tipo", "Perfil", "Razon", "RUT", "temp_id"
]

CAMPOS_PROYECTO = [
    "Nombre", "Descripcion", "MesesProy", "Area", "postulante_temp_id"
]

CAMPOS_RELACIONES = [
    "postulante_temp_id", "proyecto_nombre", "postulante_rut"
]

def extraer_json_puro(texto):
    match = re.search(r"```json\s*(\{.*?\})\s*```", texto, re.DOTALL)
    if match:
        return match.group(1)
    match = re.search(r"(\{.*\})", texto, re.DOTALL)
    if match:
        return match.group(1)
    return None

def limpiar_valor(valor):
    if isinstance(valor, str):
        valor = valor.strip()
    if isinstance(valor, float) or isinstance(valor, int):
        return valor
    if re.fullmatch(r"\d+(\.\d+)?", str(valor)):
        return float(valor) if '.' in valor else int(valor)
    if str(valor).lower() in ["sí", "si"]:
        return "Sí"
    elif str(valor).lower() == "no":
        return "No"
    return valor

def llamar_modelo_local(prompt):
    try:
        response = requests.post(
            API,
            json={
                "model": MODEL,
                "prompt": prompt,
                "stream": False,
                "options": {"temperature": 0.3, "top_p": 0.9}
            }
        )
        response.raise_for_status()
        result = response.json()
        return result.get("response", "")
    except Exception as e:
        print(f"Error al llamar al modelo local: {e}")
        return ""

def estructurar_datos(texto):
    prompt = f"""
        Eres un asistente que siempre responde solo con JSON puro, sin explicaciones ni razonamientos.

        Extrae la información solicitada del siguiente texto de un postulante a fondos concursables. La respuesta debe ser únicamente un objeto JSON válido con dos secciones: "postulante" y "proyectos".

        INSTRUCCIONES ESTRICTAS:
        1. Para el POSTULANTE:
        - Nombre: Nombre legal del grupo (100 caracteres max)
        - Creacion: Fecha en formato YYYY/MM/DD (usar "2023/01/01" si no hay info)
        - Tipo: "Persona natural", "Persona jurídica" u otro (100 caracteres max)
        - Perfil: Descripción breve basada en actividades (100 caracteres max)
        - Razon: Razón social completa
        - RUT: Formato 12.345.678-9

        2. Para PROYECTOS (1 por actividad):
        - Nombre: Nombre corto de la actividad
        - Descripcion: Detalle (300 caracteres max)
        - MesesProy: Entre 6 y 36 (default 12)
        - Area: Área principal

        FORMATO REQUERIDO:
        {{
            "postulante": {{
                "Nombre": "...",
                "Creacion": "...",
                "Tipo": "...",
                "Perfil": "...",
                "Razon": "...",
                "RUT": "..."
            }},
            "proyectos": [
                {{
                    "Nombre": "...",
                    "Descripcion": "...",
                    "MesesProy": ...,
                    "Area": "..."
                }}
            ]
        }}

        Texto a analizar:
        {texto}
    """

    raw_text = llamar_modelo_local(prompt)
    json_text = extraer_json_puro(raw_text)
    
    if not json_text:
        print("No se pudo extraer JSON del texto:")
        print(raw_text)
        return {"postulante": {}, "proyectos": []}
    
    try:
        return json.loads(json_text)
    except json.JSONDecodeError as e:
        print("Error decodificando JSON:")
        print(json_text)
        print(e)
        return {"postulante": {}, "proyectos": []}


def main():
    os.makedirs(os.path.dirname(DIR_POST), exist_ok=True)
    input_csv_path = os.path.join(BASE_DIR, "webscrape", "proyectoscorfo_raw", "boletaofactura_resultados.csv")
    df = pd.read_csv(input_csv_path)
    df = df[~df["Error"].notna()]
    postulantes_estructurados = []
    proyectos_estructurados = []
    relaciones_temp = []

    for i, row in df.iterrows():
        print(f"Procesando postulante {i+1}/{len(df)}...")
        texto_propmt = f"""
            Razón Social: {row['RazonSocial']}
            Tipo: {row['TipoSubtipo']}
            Actividades: {row['Actividades']}
            RUT: {row['RutConfirmado']}
        """
        
        data = estructurar_datos(texto_propmt)
        
        # Procesar postulante
        postulante = {
            campo: limpiar_valor(data.get("postulante", {}).get(campo, "")) 
            for campo in CAMPOS_POSTULANTE if campo != "temp_id"
        }
        postulante["temp_id"] = i + 1
        postulantes_estructurados.append(postulante)
        
        # Procesar proyectos
        for proyecto in data.get("proyectos", []):
            proyecto_limpio = {
                campo: limpiar_valor(proyecto.get(campo, "")) 
                for campo in CAMPOS_PROYECTO if campo != "postulante_temp_id"
            }
            proyecto_limpio["postulante_temp_id"] = i + 1
            proyectos_estructurados.append(proyecto_limpio)
            
            relaciones_temp.append({
                "postulante_temp_id": i + 1,
                "proyecto_nombre": proyecto_limpio.get("Nombre", ""),
                "postulante_rut": postulante.get("RUT", "")
            })

    # Guardar resultados
    df_postulantes = pd.DataFrame(postulantes_estructurados)
    df_proyectos = pd.DataFrame(proyectos_estructurados)

    # Asegurar formatos
    df_postulantes["Creacion"] = pd.to_datetime(df_postulantes["Creacion"], errors='coerce').dt.strftime('%Y/%m/%d')
    df_proyectos["MesesProy"] = pd.to_numeric(df_proyectos["MesesProy"], errors='coerce').fillna(12).astype(int)

    # Guardar archivos
    df_postulantes.to_csv(DIR_POST, index=False)
    df_proyectos.to_csv(DIR_PROY, index=False)


if __name__ == "__main__":
    main()