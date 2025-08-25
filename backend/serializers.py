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

class ProyectoForaneoSerial(serializers.ModelSerializer):
    Beneficiario = models.ForeignKey(Beneficiario, on_delete=models.CASCADE)

class PersonaSerializado(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = ('ID', 'Nombre', 'Sexo', 'RUT')

class MiembroSerializado(serializers.ModelSerializer):
    class Meta:
        model = Miembro
        fields = ('ID', 'Persona', 'Beneficiario')

class MiembroForaneoSerial(serializers.ModelSerializer):
    Persona = models.ForeignKey(Persona, on_delete=models.CASCADE)
    Beneficiario = models.ForeignKey(Beneficiario, on_delete=models.CASCADE)

class ColaboradorSerializado(serializers.ModelSerializer):
    class Meta:
        model = Colaborador
        fields = ('ID', 'Persona', 'Proyecto')

class ColaboradorForaneoSerial(serializers.ModelSerializer):
    Persona = models.ForeignKey(Persona, on_delete=models.CASCADE)
    Proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)

class UsuarioSerializado(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('ID', 'Persona', 'NombreDeUsuario', 'Contrasena', 'Correo')

class UsuarioForaneoSerial(serializers.ModelSerializer):
    Persona = models.ForeignKey(Persona, on_delete=models.CASCADE)

class ConsorcioSerializado(serializers.ModelSerializer):
    class Meta:
        model = Consorcio
        fields = ('ID', 'PrimerBeneficiario', 'SegundoBeneficiario')

class ConsorcioForaneoSerial(serializers.ModelSerializer):
    PrimerBeneficiario = models.ForeignKey(Beneficiario, on_delete=models.CASCADE, related_name='primero')
    SegundoBeneficiario = models.ForeignKey(Beneficiario, on_delete=models.CASCADE, related_name='segundo')

class FinanciadorSerializado(serializers.ModelSerializer):
    class Meta:
        model = Financiador
        fields = ('ID', 'Nombre', 'FechaDeCreacion', 'RegionDeCreacion', 'Direccion', 'TipoDePersona', 'TipoDeEmpresa', 'Perfil', 'RUTdeEmpresa', 'RUTdeRepresentante')

class InstrumentoSerializado(serializers.ModelSerializer):
    class Meta:
        model = Instrumento
        fields = ('ID', 'Titulo', 'Financiador', 'Alcance', 'Descripcion', 'FechaDeApertura', 'FechaDeCierre', 'DuracionEnMeses', 'Beneficios', 'Requisitos', 'MontoMinimo', 'MontoMaximo', 'Estado', 'TipoDeBeneficio', 'TipoDePerfil', 'EnlaceDelDetalle', 'EnlaceDeLaFoto')

class InstrumentoForaneoSerial(serializers.ModelSerializer):
    Financiador = models.ForeignKey(Financiador, on_delete=models.CASCADE)

class PostulacionSerializado(serializers.ModelSerializer):
    class Meta:
        model = Postulacion
        fields = ('ID', 'Beneficiario', 'Proyecto', 'Instrumento', 'Resultado', 'MontoObtenido', 'FechaDePostulacion', 'FechaDeResultado', 'Detalle')

class PostulacionForaneoSerial(serializers.ModelSerializer):
    Beneficiario = models.ForeignKey(Beneficiario, null=False, on_delete=models.CASCADE)
    Proyecto = models.ForeignKey(Proyecto, null=False, on_delete=models.CASCADE)
    Instrumento = models.ForeignKey(Instrumento, on_delete=models.CASCADE)
