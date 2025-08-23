from rest_framework import serializers
from .models import *

class BeneficiarioSerializado(serializers.ModelSerializer):
    class Meta:
        model = Beneficiario
        fields = ('ID', 'Nombre', 'FechaDeCreacion', 'RegionDeCreacion', 'Direccion', 'TipoDePersona', 'TipoDeEmpresa', 'Perfil', 'RUTdeEmpresa', 'RUTdeRepresentante')

class ProyectoSerializado(serializers.ModelSerializer):
    class Meta:
        model = Proyecto
        fields = ('ID', 'Beneficiario', 'Titulo', 'Descripcion', 'DuracionEnMesesMinimo', 'DuracionEnMesesMaximo', 'Alcance', 'Area')

class PersonaSerializado(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = ('ID', 'Nombre', 'Sexo', 'RUT')

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
        fields = ('ID', 'Nombre', 'FechaDeCreacion', 'RegionDeCreacion', 'Direccion', 'TipoDePersona', 'TipoDeEmpresa', 'Perfil', 'RUTdeEmpresa', 'RUTdeRepresentante')

class InstrumentoSerializado(serializers.ModelSerializer):
    class Meta:
        model = Instrumento
        fields = ('ID', 'Titulo', 'Financiador', 'Alcance', 'Descripcion', 'FechaDeApertura', 'FechaDeCierre', 'DuracionEnMeses', 'Beneficios', 'Requisitos', 'MontoMinimo', 'MontoMaximo', 'Estado', 'TipoDeBeneficio', 'TipoDePerfil', 'EnlaceDelDetalle', 'EnlaceDeLaFoto')

class PostulacionSerializado(serializers.ModelSerializer):
    class Meta:
        model = Postulacion
        fields = ('ID', 'Beneficiario', 'Proyecto', 'Instrumento', 'Resultado', 'MontoObtenido', 'FechaDePostulacion', 'FechaDeResultado', 'Detalle')
