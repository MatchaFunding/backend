from rest_framework import serializers
from .models import *

'''
class BeneficiarioSerial(serializers.ModelSerializer):
    class Meta:
        model = Beneficiario
        fields = ('ID','Nombre','Creacion','Tipo','Perfil','Razon','RUT')
 
class ProyectoSerial(serializers.ModelSerializer):
    class Meta:
        model = Proyecto
        fields = ('ID','IDPost','Nombre','Descripcion','MesesProy','Area')
 
class MiembroSerial(serializers.ModelSerializer):
    class Meta:
        model = Miembro
        fields = ('ID','IDPost','Nombre','RUT','Curriculum','Genero')

class FinanciadorSerial(serializers.ModelSerializer):
    class Meta:
        model = Financiador
        fields = ('ID','Institucion','Tipo')

class FondoSerial(serializers.ModelSerializer):
    class Meta:
        model = Fondo
        fields = ('ID','IDFinan','Titulo','Alcance','TipoPersona','Descripcion','Apertura','Cierre','MesesProy','Requisito','MontoMin','MontoMax','Beneficios','Foco','Intervencion','Instrumento','InstHomologado')
 
class PostulacionSerial(serializers.ModelSerializer):
    class Meta:
        model = Postulacion
        fields = ('ID','IDProy','IDFond')

class ResultadoSerial(serializers.ModelSerializer):
    class Meta:
        model = Resultado
        fields = ('ID','IDPost','IDFond','Estado','Monto','Emision','Detalle')

class PaginaDelFondoSerial(serializers.ModelSerializer):
    class Meta:
        model = PaginaDelFondo
        fields = ('ID','IDFond','LinkPagina','LinkPostula','LinkFoto')

class UsuarioPostSerial(serializers.ModelSerializer):
    class Meta:
        model = UsuarioPost
        fields = ('ID','IDPost','Correo','Nombre','Clave')
        
class FinanciadorSerial(serializers.ModelSerializer):
    class Meta:
        model = Financiador
        fields = ('ID','Institucion','Tipo')
'''