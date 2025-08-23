import os
import sys
import pandas as pd
import json
import re
import requests
import django
from datetime import datetime

# CONFIGURACIÓN DJANGO
# --------------------------------------------------
script_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(script_dir)

sys.path.append(project_root)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()

from backend.models import Beneficiario, Proyecto
# --------------------------------------------------

# Configuración de Ollama
API = "http://localhost:11434/api/generate"
MODEL = "llama3.2:latest"
#MODEL = "gemma3:latest"

DIR_SUCIO = os.path.join(script_dir, 'datos', 'sucios', 'csvs', 'boletaofactura_resultados.csv')

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
    # Buscar JSON en el texto, manejando diferentes formatos
    match = re.search(r"```json\s*(\{.*?\})\s*```", texto, re.DOTALL)
    if not match:
        match = re.search(r"(\{.*\})", texto, re.DOTALL)
    return match.group(1) if match else None

def procesar_fila(row):
    # Crear el texto a analizar combinando las columnas relevantes
    texto_analizar = f"""
    Razon Social: {row.get('RazonSocial', '')}
    Tipo/Subtipo: {row.get('TipoSubtipo', '')}
    Actividades: {row.get('Actividades', '')}
    RUT: {row.get('RUT', row.get('RutConfirmado', ''))}
    """
    
    prompt = f"""
        Eres un asistente que siempre responde solo con JSON puro, sin explicaciones ni razonamientos.
        Extrae la información solicitada del siguiente texto de beneficiarios y proyectos de estos. 
        La respuesta debe ser únicamente un objeto JSON válido.

        INSTRUCCIONES ESTRICTAS:
        1. Para el BENEFICIARIO:
        - Nombre: Nombre legal del grupo (100 caracteres max) - usar Razon Social
        - TipoPersona: "NA" para Persona natural o "JU" para Persona jurídica - inferir de Tipo/Subtipo
        - TipoDeEmpresa: "SA", "SRL", "SPA", "EIRL" - inferir de Tipo/Subtipo
        - Perfil: "EMP", "EXT", "INS", "MED", "ORG", "PER" - inferir del contexto
        - RUT: Formato 12.345.678-9 - usar el RUT proporcionado

        2. Para PROYECTOS (1 por actividad):
        - Titulo: Nombre corto basado en las actividades
        - Descripcion: Detalle de la actividad (300 caracteres max)
        - Area: Contextual del proyecto basado en las actividades

        FORMATO REQUERIDO:
        {{
            "beneficiario": {{
                "Nombre": "...",
                "TipoPersona": "...",
                "TipoDeEmpresa": "...",
                "Perfil": "...",
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
        
        Texto a analizar:
        {texto_analizar}
    """

    print(f"Enviando prompt para: {row.get('RazonSocial', '')}")
    raw = llamar_modelo_local(prompt)
    
    if not raw:
        print(f"No se obtuvo respuesta del modelo para: {row.get('RazonSocial', '')}")
        return None, []
    
    json_text = extraer_json_puro(raw)
    if not json_text:
        print(f"No se pudo extraer JSON de la respuesta: {raw[:200]}...")
        return None, []

    try:
        data = json.loads(json_text)
    except json.JSONDecodeError as e:
        print(f"Error decodificando JSON: {e}")
        print(f"Texto JSON: {json_text}")
        return None, []

    # Crear beneficiario
    b_data = data.get("beneficiario", {})
    tipo_persona, tipo_empresa, perfil = mapear_choices(
        b_data.get("TipoPersona", ""),
        b_data.get("TipoDeEmpresa", ""),
        b_data.get("Perfil", "")
    )
    
    # Usar RUT del JSON o del CSV
    rut_json = b_data.get("RUT", "")
    rut_csv = row.get('RUT', row.get('RutConfirmado', ''))
    rut = rut_json if rut_json else rut_csv

    # Validar que el beneficiario no exista ya
    if Beneficiario.objects.filter(RUTdeEmpresa=rut).exists():
        print(f"Beneficiario con RUT {rut} ya existe, saltando...")
        return None, []

    # Usar fecha fija 2025/01/01 como solicitaste
    fecha_creacion = datetime.strptime("2025/01/01", "%Y/%m/%d").date()

    beneficiario = Beneficiario(
        Nombre=b_data.get("Nombre", row.get('RazonSocial', '')[:100]),
        FechaDeCreacion=fecha_creacion,  # Fecha fija
        RegionDeCreacion="RM",
        Direccion="N/A",
        TipoDePersona=tipo_persona,
        TipoDeEmpresa=tipo_empresa,
        Perfil=perfil,
        RUTdeEmpresa=rut,
        RUTdeRepresentante=rut  # Mismo RUT por defecto
    )
    
    try:
        beneficiario.save()
        print(f"Beneficiario guardado: {beneficiario.Nombre}")
    except Exception as e:
        print(f"Error guardando beneficiario: {e}")
        import traceback
        traceback.print_exc()
        return None, []

    # Crear proyectos asociados
    proyectos_guardados = []
    proyectos_data = data.get("proyectos", [])
    
    if not proyectos_data:
        # Si no hay proyectos en el JSON, crear uno por defecto basado en actividades
        actividades = row.get('Actividades', '')
        proyecto_default = {
            "Titulo": f"Proyecto {row.get('RazonSocial', '')[:20]}",
            "Descripcion": f"Proyecto basado en actividades: {actividades[:200]}",
            "Area": "Desarrollo"  # Valor por defecto
        }
        proyectos_data = [proyecto_default]

    for p in proyectos_data:
        proyecto = Proyecto(
            Beneficiario=beneficiario,
            Titulo=p.get("Titulo", "Proyecto sin título")[:300],
            Descripcion=p.get("Descripcion", "Sin descripción")[:500],
            DuracionEnMesesMinimo=6,
            DuracionEnMesesMaximo=12,
            Alcance="RM",
            Area=p.get("Area", "Investigación")[:100]
        )
        try:
            proyecto.save()
            proyectos_guardados.append(proyecto)
            print(f"  Proyecto guardado: {proyecto.Titulo}")
        except Exception as e:
            print(f"Error guardando proyecto: {e}")
            import traceback
            traceback.print_exc()

    return beneficiario, proyectos_guardados

def main():
    try:
        df = pd.read_csv(DIR_SUCIO)
        print(f"CSV cargado. Columnas: {list(df.columns)}")
        print(f"Primeras filas:\n{df.head()}")
        
        # Filtrar filas sin error
        if "Error" in df.columns:
            df = df[df["Error"].isna()]
        print(f"Filas a procesar: {len(df)}")
        
        for i, row in df.iterrows():
            print(f"\n--- Procesando fila {i+1}/{len(df)}: {row.get('RazonSocial', 'N/A')} ---")
            try:
                beneficiario, proyectos = procesar_fila(row)
                if beneficiario:
                    print(f"✅ Procesado exitosamente: {beneficiario.Nombre}")
                    print(f"   Proyectos creados: {len(proyectos)}")
                else:
                    print("❌ No se pudo procesar la fila")
            except Exception as e:
                print(f"❌ Error procesando fila {i}: {e}")
                import traceback
                traceback.print_exc()
                
    except Exception as e:
        print(f"Error cargando CSV: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
