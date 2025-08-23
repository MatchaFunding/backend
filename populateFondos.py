import os
import django
import pandas as pd
from datetime import datetime

# Configuración de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()

from backend.models import Instrumento, Financiador


# ---- Config paths ----
BASE_DIR = os.path.dirname(__file__)
CSV_LIMPIOS_DIR = os.path.join(BASE_DIR, "datos", "limpios", "csvs")

CSV_FILES = {
    "ANID": os.path.join(CSV_LIMPIOS_DIR, "abiertos-anid-limpio.csv"),
    "CORFO": os.path.join(CSV_LIMPIOS_DIR, "abiertos-corfo-limpio.csv"),
    "FondosGob": os.path.join(CSV_LIMPIOS_DIR, "abiertos-fondosgob-limpio.csv"),
}

# ---- Helpers ----
def parse_date(fecha_str):
    try:
        return datetime.strptime(str(fecha_str), "%Y-%m-%d").date()
    except Exception:
        return None

def parse_int(valor):
    try:
        return int(valor)
    except Exception:
        return None

def truncar(cadena, max_len):
    return str(cadena)[:max_len] if pd.notna(cadena) else ""


# ---- Main inserter ----
def poblar(csv_path, fuente):
    df = pd.read_csv(csv_path, quotechar='"')
    print(f"\n📂 Procesando {fuente} ({len(df)} fondos)")

    for idx, row in df.iterrows():
        try:
            # --- manejar financiador (solo primero) ---
            financiadores_raw = str(row.get("Financiador", "")).split(",")
            financ = financiadores_raw[0].strip() if financiadores_raw[0].strip() else "Desconocido"

            # Crear o recuperar financiador
            financiador_obj, _ = Financiador.objects.get_or_create(
                Nombre=truncar(financ, 100),
                defaults={
                    "FechaDeCreacion": datetime.today().date(),
                    "RegionDeCreacion": "RM",
                    "Direccion": "N/A",
                    "TipoDePersona": "JU",
                    "TipoDeEmpresa": "SA",
                    "Perfil": "INS",
                    "RUTdeEmpresa": "00000000-0",
                    "RUTdeRepresentante": "00000000-0"
                }
            )

            # Crear el instrumento
            instrumento = Instrumento(
                Titulo=truncar(row["Titulo"], 200),
                Financiador=financiador_obj,
                Alcance=truncar(row["Alcance"], 30),
                Descripcion=truncar(row["Descripcion"], 1000),
                FechaDeApertura=parse_date(row["Apertura"]),
                FechaDeCierre=parse_date(row["Cierre"]),
                DuracionEnMeses=parse_int(row["MesesProy"]),
                Beneficios=truncar(row["Beneficios"], 1000),
                Requisitos=truncar(row["Requisitos"], 1000),
                MontoMinimo=parse_int(row["MontoMin"]),
                MontoMaximo=parse_int(row["MontoMax"]),
                Estado=truncar(row["Estado"], 30),
                TipoDeBeneficio=truncar(row["TipoDeBeneficio"], 30),
                TipoDePerfil=truncar(row["TipoPersona"], 30),
                EnlaceDelDetalle=truncar(row["EnlaceDelDetalle"], 300),
                EnlaceDeLaFoto=truncar(row["EnlaceDeLaFoto"], 300),
            )
            instrumento.save()

            print(f"  ✅ [{fuente}] Fondo {idx+1}/{len(df)} insertado (financiador: {financ})")

        except Exception as e:
            print(f"  ❌ Error en fila {idx+1}: {e}")


if __name__ == "__main__":
    for fuente, path in CSV_FILES.items():
        poblar(path, fuente)

    print("\n🚀 Inserción completada.")
