import os
import pandas as pd
import json
import re
import requests
import django
from datetime import datetime
from django.db import transaction

# Configurar el entorno de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()

from databases.backend.models import Beneficiario, Proyecto, Ubicacion

# Configuración del modelo IA local
API = "http://localhost:11434/api/generate"
MODEL = "llama3.2:latest"

PERSONA = {"JU": "Juridica", "NA": "Natural"}
EMPRESA = {"SA": "Sociedad Anonima",
           "SRL": "Sociedad de Responsabilidad Limitada",
           "SPA": "Sociedad por Acciones",
           "EIRL": "Empresa Individual de Responsabilidad Limitada"}
PERFIL = {"EMP": "Empresa", "EXT": "Extranjero", "INS": "Institucion",
          "MED": "Intermediario", "ORG": "Organizacion", "PER": "Persona"}

# Funciones helper
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
    tipo_persona_mapped = "JU" if "juridica" in tipo_persona.lower() else "NA"
    tipo_empresa_mapped = "EIRL"
    for k, v in EMPRESA.items():
        if v.lower() in tipo_empresa.lower():
            tipo_empresa_mapped = k
            break
    perfil_mapped = "EMP"
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

# Main masivo
def main():
    df = pd.read_csv("scripts/proyectos.csv")
    df = df[df["Error"].isna()]
    df = df.dropna(subset=["RazonSocial", "Texto", "RutConfirmado"])  # Saltar filas incompletas
    df = df[df["RazonSocial"].str.strip() != ""]
    df = df[df["Texto"].str.strip() != ""]

    lugar_rm = Ubicacion.objects.get(codigo="RM")
    beneficiarios_bulk = []
    proyectos_bulk = []

    with transaction.atomic():  # Asegura rollback si hay error
        for i, row in df.iterrows():
            prompt = f"""
                Eres un asistente que siempre responde solo con JSON puro.
                Extrae Beneficiario y Proyectos:
                {row['Texto']}
            """
            raw = llamar_modelo_local(prompt)
            json_text = extraer_json_puro(raw)
            if not json_text:
                print(f"No se pudo extraer JSON fila {i+1}")
                continue

            try:
                data = json.loads(json_text)
                b_data = data.get("beneficiario", {})
                tipo_persona, tipo_empresa, perfil = mapear_choices(
                    b_data.get("TipoPersona", ""), b_data.get("TipoDeEmpresa", ""), b_data.get("Perfil", "")
                )
                rut = b_data.get("RUT", row["RutConfirmado"])
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
                beneficiarios_bulk.append(beneficiario)

                # Proyectos
                for p in data.get("proyectos", []):
                    proyecto = Proyecto(
                        Beneficiario=beneficiario,  # Se asignará tras bulk_save
                        Titulo=p.get("Titulo", ""),
                        Descripcion=p.get("Descripcion", ""),
                        DuracionEnMesesMinimo=6,
                        DuracionEnMesesMaximo=12,
                        Alcance=lugar_rm,
                        Area=p.get("Area", "Investigación")
                    )
                    proyectos_bulk.append(proyecto)

            except Exception as e:
                print(f"Error procesando fila {i+1}: {e}")

        # Guardado masivo
        Beneficiario.objects.bulk_create(beneficiarios_bulk)
        
        # Actualizar la relación FK en proyectos
        for proyecto, beneficiario in zip(proyectos_bulk, beneficiarios_bulk * len(proyectos_bulk)//len(beneficiarios_bulk)):
            proyecto.Beneficiario = beneficiario
        Proyecto.objects.bulk_create(proyectos_bulk)

if __name__ == "__main__":
    main()
