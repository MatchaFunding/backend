from rest_framework import serializers
from .models import *

class UbicacionSerializado(serializers.ModelSerializer):
    class Meta:
        model = Ubicacion
        fields = ('REGIONES', 'CAPITALES', 'ID', 'Region', 'Capital', 'Calle', 'Numero')

class BeneficiarioSerializado(serializers.ModelSerializer):
    class Meta:
        model = Beneficiario
        fields = ('PERSONA', 'EMPRESA', 'PERFIL', 'ID', 'Nombre', 'FechaDeCreacion', 'LugarDeCreacion', 'TipoDePersona', 'TipoDeEmpresa', 'Perfil', 'RUTdeEmpresa', 'RUTdeRepresentante')

class ProyectoSerializado(serializers.ModelSerializer):
    class Meta:
        model = Proyecto
        fields = ('ID', 'Beneficiario', 'Titulo', 'Descripcion', 'DuracionEnMesesMinimo', 'DuracionEnMesesMaximo', 'Alcance', 'Area')

class PersonaSerializado(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = ('SEXO', 'ID', 'Nombre', 'Sexo', 'RUT')

class MiembroSerializado(serializers.ModelSerializer):
    class Meta:
        model = Miembro
        fields = ('ID', 'Persona', 'Beneficiario')

class ColaboradorSerializado(serializers.ModelSerializer):
    class Meta:
        model = Colaborador
        fields = ('ID', 'Persona', 'Proyecto')

class UsuarioSerializado(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('ID', 'Persona', 'NombreDeUsuario', 'Contrasena', 'Correo')

class ConsorcioSerializado(serializers.ModelSerializer):
    class Meta:
        model = Consorcio
        fields = ('ID', 'PrimerBeneficiario', 'SegundoBeneficiario')

class FinanciadorSerializado(serializers.ModelSerializer):
    class Meta:
        model = Financiador
        fields = ('ID', 'Institucion', 'Tipo')

class InstrumentoSerializado(serializers.ModelSerializer):
    class Meta:
        model = Instrumento
        fields = ('ESTADO', 'BENEFICIO', 'PERSONA', 'ID', 'Titulo', 'Financiador', 'Alcance', 'Descripcion', 'FechaDeApertura', 'FechaDeCierre', 'DuracionEnMeses', 'Beneficios', 'Requisitos', 'MontoMinimo', 'MontoMaximo', 'Estado', 'TipoDeBeneficio', 'TipoDePerfil', 'EnlaceDelDetalle', 'EnlaceDeLaFoto')

class PostulacionSerializado(serializers.ModelSerializer):
    class Meta:
        model = Postulacion
        fields = ('RESULTADO', 'ID', 'Beneficiario', 'Proyecto', 'Instrumento', 'Resultado', 'MontoObtenido', 'FechaDePostulacion', 'FechaDeResultado', 'Detalle')
