import os
import sys
import pandas as pd
import json
import re
import requests
import django
from datetime import datetime

# CONFIGURACIÓN DJANGO - AGREGAR AL INICIO DEL SCRIPT
# --------------------------------------------------
# Obtener la ruta absoluta al directorio del script
script_dir = os.path.dirname(os.path.abspath(__file__))
# Subir un nivel para llegar al directorio que contiene 'backend'
project_root = os.path.dirname(script_dir)

# Agregar el directorio del proyecto al path de Python
sys.path.append(project_root)

# Establecer la variable de entorno para Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')

# Configurar Django
django.setup()

# Ahora importamos los modelos DESPUÉS de configurar Django
from backend.models import Beneficiario, Proyecto, Ubicacion

# Configuración de Ollama
API = "http://localhost:11434/api/generate"
MODEL = "llama3.2:latest"

DIR_SUCIO = os.path.join(project_root, 'datos', 'sucios', 'csvs', 'boletaofactura_resultados.csv')

# Constantes de choices
PERSONA = {"JU": "Juridica", "NA": "Natural"}
EMPRESA = {"SA": "Sociedad Anonima",
           "SRL": "Sociedad de Responsabilidad Limitada",
           "SPA": "Sociedad por Acciones",
           "EIRL": "Empresa Individual de Responsabilidad Limitada"}
PERFIL = {"EMP": "Empresa", "EXT": "Extranjero", "INS": "Institucion",
          "MED": "Intermediario", "ORG": "Organizacion", "PER": "Persona"}

def llamar_modelo_local(prompt):
    try:
        resp = requests.post(API, json={
            "model": MODEL,
            "prompt": prompt,
            "stream": False,
            "options": {"temperature": 0.3, "top_p": 0.9}
        })
        resp.raise_for_status()
        return resp.json().get("response", "")
    except Exception as e:
        print("Error llamando modelo:", e)
        return ""
    
def mapear_choices(tipo_persona, tipo_empresa, perfil):
    # Mapea strings libres a choices válidos
    tipo_persona_mapped = "JU" if "juridica" in tipo_persona.lower() else "NA"
    tipo_empresa_mapped = "EIRL"  # default
    for k, v in EMPRESA.items():
        if v.lower() in tipo_empresa.lower():
            tipo_empresa_mapped = k
            break
    perfil_mapped = "EMP"  # default
    for k, v in PERFIL.items():
        if v.lower() in perfil.lower():
            perfil_mapped = k
            break
    return tipo_persona_mapped, tipo_empresa_mapped, perfil_mapped

def extraer_json_puro(texto):
    match = re.search(r"```json\s*(\{.*?\})\s*```", texto, re.DOTALL)
    if not match:
        match = re.search(r"(\{.*\})", texto, re.DOTALL)
    return match.group(1) if match else None

def procesar_fila(row):
    prompt = f"""
        Eres un asistente que siempre responde solo con JSON puro, sans explicaciones ni razonamientos.
        Extrae la información solicitada del siguiente texto de beneficiarios y proyectos de estos. La respuesta debe ser únicamente un objeto JSON válido.

        Extrae en JSON para modelos Django los siguientes campos:

        INSTRUCCIONES ESTRICTAS:
        1. Para el BENEFICIARIO:
        - Nombre: Nombre legal del grupo (100 caracteres max)
        - TipoPersona: "NA" para Persona natural o "JU" para Persona jurídica
        - TipoDeEmpresa: "SA", "SRL", "SPA", "EIRL"
        - Perfil: "EMP", "EXT", "INS", "MED", "ORG", "PER"
        - RUT: Formato 12.345.678-9

        2. Para PROYECTOS (1 por actividad):
        - Titulo: Nombre corto de la actividad
        - Descripcion: Detalle (300 caracteres max)
        - Area: Contextual del proyecto, Investigación, Desarrollo, etc.

        FORMATO REQUERIDO:
        {{
            "beneficiario": {{
                "Nombre": "...",
                "TipoPersona": "...",
                "TipoDeEmpresa": "...",
                "Perfil": "...",
                "Razon": "...",
                "RUT": "..."
            }},
            "proyectos": [
                {{
                    "Titulo": "...",
                    "Descripcion": "...",
                    "Area": "..."
                }}
            ]
        }}
        {row['Texto']}
    """

    raw = llamar_modelo_local(prompt)
    json_text = extraer_json_puro(raw)
    if not json_text:
        print(f"No se pudo extraer JSON de la fila: {row['Texto']}")
        return None, []

    data = json.loads(json_text)

    # Obtener clave foránea de Ubicacion
    lugar_rm = Ubicacion.objects.get(codigo="RM")

    # Crear beneficiario con campos asignados manualmente
    b_data = data.get("beneficiario", {})
    tipo_persona, tipo_empresa, perfil = mapear_choices(
        b_data.get("TipoPersona", ""),
        b_data.get("TipoDeEmpresa", ""),
        b_data.get("Perfil", "")
    )
    rut = b_data.get("RUT", "")

    beneficiario = Beneficiario(
        Nombre=b_data.get("Nombre", b_data.get("Razon", "")),
        FechaDeCreacion=datetime.strptime("2025/01/01", "%Y/%m/%d").date(),
        LugarDeCreacion=lugar_rm,
        TipoDePersona=tipo_persona,
        TipoDeEmpresa=tipo_empresa,
        Perfil=perfil,
        RUTdeEmpresa=rut,
        RUTdeRepresentante=rut
    )
    beneficiario.save()

    # Crear proyectos asociados
    proyectos_guardados = []
    for p in data.get("proyectos", []):
        proyecto = Proyecto(
            Beneficiario=beneficiario,
            Titulo=p.get("Titulo", ""),
            Descripcion=p.get("Descripcion", ""),
            DuracionEnMesesMinimo=6,
            DuracionEnMesesMaximo=12,
            Alcance=lugar_rm,
            Area=p.get("Area", "Investigación")
        )
        proyecto.save()
        proyectos_guardados.append(proyecto)

    return beneficiario, proyectos_guardados

def main():
    df = pd.read_csv(DIR_SUCIO)
    df = df[df["Error"].isna()]  # Ignorar filas con error

    for i, row in df.iterrows():
        print(f"Procesando fila {i+1}/{len(df)}: {row['RazonSocial']}")
        try:
            procesar_fila(row)
        except Exception as e:
            print(f"Error procesando fila {i}: {e}")

if __name__ == "__main__":
    main()