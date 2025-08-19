from django.http import JsonResponse
from django.db import connection
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import *
from .models import *
import requests
import json
from django.db.models import *

'''
@api_view(['GET'])
def VerTodosLosBeneficiarios(request):
    result = Beneficiario.objects.all()
    serializer = BeneficiarioSerial(result, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def EnviarNuevoBeneficiario(request):
    if request.method == 'POST':
        serializer = BeneficiarioSerial(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        # ----- ESTA ES LA LÍNEA QUE HAY QUE CORREGIR -----
        # En lugar de devolver serializer.data (que da error), devolvemos serializer.errors
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # Esta parte de abajo en realidad nunca se alcanza, pero la dejamos por si acaso.
    return Response({"error": "Método no POST no manejado"}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def BuscarBeneficiarioPorID(request):
    id = request.data.get('ID')
    result = Beneficiario.objects.filter(ID=id)
    serializer = BeneficiarioSerial(result, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def VerTodosLosProyectos(request):
    result = Proyecto.objects.all()
    serializer = ProyectoSerial(result, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def BuscarProyectosPorPost(request):
    id = request.data.get('ID')
    result = Proyecto.objects.filter(IDPost=id)
    serializer = ProyectoSerial(result, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def EnviarNuevoProyecto(request):
    if request.method == 'POST':
        serializer = ProyectoSerial(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def VerTodosLosMiembros(request):
    result = Miembro.objects.all()
    serializer = MiembroSerial(result, many=True)
    return Response(serializer.data)

@api_view(['GET']) # Esta ya la tenías
def VerTodosLosFinanciadores(request):
    result = Financiador.objects.all()
    serializer = FinanciadorSerial(result, many=True)
    return Response(serializer.data)

@api_view(['POST']) # NUEVA VISTA para crear financiadores
def EnviarNuevoFinanciador(request):
    if request.method == 'POST':
        serializer = FinanciadorSerial(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    # Por si acaso, aunque @api_view(['POST']) ya lo restringe
    return Response({"detail": "Método no permitido para esta URL."}, status=status.HTTP_405_METHOD_NOT_ALLOWED)




@api_view(['GET'])
def VerTodosLosFondos(request):
    result = Fondo.objects.all()
    serializer = FondoSerial(result, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def EnviarNuevoFondo(request):
    if request.method == 'POST':
        serializer = FondoSerial(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def VerTodasLasPostulaciones(request):
    result = Postulacion.objects.all()
    serializer = PostulacionSerial(result, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def EnviarNuevaPostulacion(request):
    if request.method == 'POST':
        serializer = PostulacionSerial(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def VerTodosLosResultados(request):
    result = Resultado.objects.all()
    serializer = ResultadoSerial(result, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def VerTodasLasPaginasDeFondos(request):
    result = PaginaDelFondo.objects.all()
    serializer = PaginaDelFondoSerial(result, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def VerTodosLosUsuarioPost(request):
    result = UsuarioPost.objects.all()
    serializer = UsuarioPostSerial(result, many=True)
    return Response(serializer.data)


@api_view(['POST']) 
def EnviarNuevoResultado(request): 
    if request.method == 'POST':
        serializer = ResultadoSerial(data=request.data) 
        if serializer.is_valid(): 
            serializer.save() 
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response({"detail": "Método no permitido"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['POST'])
def ValidarCredencialesDeUsuarioPost(request):
    print("Datos recibidos:", request.data)
    user_input = request.data.get('Usuario') 
    password = request.data.get('Clave')
    result = UsuarioPost.objects.filter(
        Clave=password
    ).filter(
        (Q(Nombre=user_input) | Q(Correo=user_input))
    )
    print("Resultado de la consulta:", result)
    serializer = UsuarioPostSerial(result, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def RegistrarNuevoUsuarioPost(request):
    if request.method == 'POST':
        serializer = UsuarioPostSerial(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def VerTodosLosProyectosPorIDPost(request):
    Beneficiario_id_str = request.data.get('ID')

    if Beneficiario_id_str is None:
        return Response({"error": "El campo 'ID' (ID del Beneficiario) es requerido en el cuerpo de la solicitud."}, status=status.HTTP_400_BAD_REQUEST)
    
    try:
     
        Beneficiario_id = int(Beneficiario_id_str)
    except ValueError:
        return Response({"error": "El 'ID' del Beneficiario debe ser un número entero."}, status=status.HTTP_400_BAD_REQUEST)
    
    try:
        result = Proyecto.objects.filter(IDPost=Beneficiario_id)
    except FieldError as e:
       
        return Response({"error": f"Error en el campo de filtrado del modelo Proyecto: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    serializer = ProyectoSerial(result, many=True)
    return Response(serializer.data)

@api_view(['PUT']) 
def ActualizarBeneficiario(request, pk=None):
    Beneficiario_id_str = request.data.get('ID', pk) 

    if Beneficiario_id_str is None:
        return Response({"error": "ID del Beneficiario no proporcionado."}, status=status.HTTP_400_BAD_REQUEST)
    
    try:
        Beneficiario_id = int(Beneficiario_id_str)
    except ValueError:
        return Response({"error": "ID del Beneficiario debe ser un número."}, status=status.HTTP_400_BAD_REQUEST)

    try:
        Beneficiario_instance = Beneficiario.objects.get(ID=Beneficiario_id)
    except Beneficiario.DoesNotExist:
        return Response({"error": "Beneficiario no encontrado."}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
       
        serializer = BeneficiarioSerial(Beneficiario_instance, data=request.data, partial=True) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    return Response({"detail": "Método no permitido."}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

'''