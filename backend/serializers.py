from rest_framework import serializers
from .models import *

class UbicacionSerializado(serializers.ModelSerializer):
    class Meta:
        model = Ubicacion
        fields = ('REGIONES', 'CAPITALES', 'ID', 'Region', 'Capital', 'Calle', 'Numero')

class PersonaSerializado(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = ('SEXO', 'ID', 'Nombre', 'Sexo', 'RUT')

class MiembroDeUnaEmpresaSerializado(serializers.ModelSerializer):
    class Meta:
        model = MiembroDeUnaEmpresa
        fields = ('ID', 'Persona', 'Beneficiario')

class MiembroDeProyectoSerializado(serializers.ModelSerializer):
    class Meta:
        model = MiembroDeProyecto
        fields = ('ID', 'Persona', 'Proyecto')

class UsuarioDeMatchaFundingSerializado(serializers.ModelSerializer):
    class Meta:
        model = UsuarioDeMatchaFunding
        fields = ('ID', 'Persona', 'NombreDeUsuario', 'Contrasena', 'Correo')

class BeneficiarioSerializado(serializers.ModelSerializer):
    class Meta:
        model = Beneficiario
        fields = ('PERSONA', 'EMPRESA', 'PERFIL', 'ID', 'Nombre', 'FechaDeCreacion', 'LugarDeCreacion', 'TipoDePersona', 'TipoDeEmpresa', 'Perfil', 'RUTdeEmpresa', 'RUTdeRepresentante')

class ConsorcioDeBeneficiariosSerializado(serializers.ModelSerializer):
    class Meta:
        model = ConsorcioDeBeneficiarios
        fields = ('ID', 'PrimerBeneficiario', 'SegundoBeneficiario')

class ProyectoSerializado(serializers.ModelSerializer):
    class Meta:
        model = Proyecto
        fields = ('ID', 'Beneficiario', 'Titulo', 'Descripcion', 'DuracionEnMesesMinimo', 'DuracionEnMesesMaximo', 'Alcance', 'Area')

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
