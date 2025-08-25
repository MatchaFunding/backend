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

@api_view(['GET'])
def VerTodosLosBeneficiarios(request):
    result = Beneficiario.objects.all()
    serializer = BeneficiarioSerializado(result, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def CrearBeneficiario(request):
    if request.method == 'POST':
        serializer = BeneficiarioSerializado(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def CambiarBeneficiario(request, pk=None):
    try:
        instance = Beneficiario.objects.get(pk=pk)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_404_NOT_FOUND)

    serializer = BeneficiarioSerializado(instance, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def BorrarBeneficiario(request, pk=None):
    member = Beneficiario.objects.get(pk=pk)
    member.delete()
    return Response(status=status.HTTP_200_OK)

@api_view(['GET'])
def VerTodosLosProyectos(request):
    result = Proyecto.objects.all()
    serializer = ProyectoSerializado(result, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def CrearProyecto(request):
    if request.method == 'POST':
        serializer = ProyectoSerializado(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def CambiarProyecto(request, pk=None):
    try:
        instance = Proyecto.objects.get(pk=pk)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_404_NOT_FOUND)

    serializer = ProyectoSerializado(instance, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def BorrarProyecto(request, pk=None):
    member = Proyecto.objects.get(pk=pk)
    member.delete()
    return Response(status=status.HTTP_200_OK)

@api_view(['GET'])
def VerTodasLasPersonas(request):
    result = Persona.objects.all()
    serializer = PersonaSerializado(result, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def CrearPersona(request):
    if request.method == 'POST':
        serializer = PersonaSerializado(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def CambiarPersona(request, pk=None):
    try:
        instance = Persona.objects.get(pk=pk)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_404_NOT_FOUND)

    serializer = PersonaSerializado(instance, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def BorrarPersona(request, pk=None):
    member = Persona.objects.get(pk=pk)
    member.delete()
    return Response(status=status.HTTP_200_OK)

@api_view(['GET'])
def VerTodosLosMiembros(request):
    result = Miembro.objects.all()
    serializer = MiembroSerializado(result, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def CrearMiembro(request):
    if request.method == 'POST':
        serializer = MiembroSerializado(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def CambiarMiembro(request, pk=None):
    try:
        instance = Miembro.objects.get(pk=pk)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_404_NOT_FOUND)

    serializer = MiembroSerializado(instance, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def BorrarMiembro(request, pk=None):
    member = Miembro.objects.get(pk=pk)
    member.delete()
    return Response(status=status.HTTP_200_OK)

@api_view(['GET'])
def VerTodosLosColaboradores(request):
    result = Colaborador.objects.all()
    serializer = ColaboradorSerializado(result, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def CrearColaborador(request):
    if request.method == 'POST':
        serializer = ColaboradorSerializado(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def CambiarColaborador(request, pk=None):
    try:
        instance = Colaborador.objects.get(pk=pk)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_404_NOT_FOUND)

    serializer = ColaboradorSerializado(instance, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def BorrarColaborador(request, pk=None):
    member = Colaborador.objects.get(pk=pk)
    member.delete()
    return Response(status=status.HTTP_200_OK)

@api_view(['GET'])
def VerTodosLosUsuarios(request):
    result = Usuario.objects.all()
    serializer = UsuarioSerializado(result, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def CrearUsuario(request):
    if request.method == 'POST':
        serializer = UsuarioSerializado(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def CambiarUsuario(request, pk=None):
    try:
        instance = Usuario.objects.get(pk=pk)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_404_NOT_FOUND)

    serializer = UsuarioSerializado(instance, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def BorrarUsuario(request, pk=None):
    member = Usuario.objects.get(pk=pk)
    member.delete()
    return Response(status=status.HTTP_200_OK)

@api_view(['GET'])
def VerTodosLosConsorcios(request):
    result = Consorcio.objects.all()
    serializer = ConsorcioSerializado(result, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def CrearConsorcio(request):
    if request.method == 'POST':
        serializer = ConsorcioSerializado(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def CambiarConsorcio(request, pk=None):
    try:
        instance = Consorcio.objects.get(pk=pk)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_404_NOT_FOUND)

    serializer = ConsorcioSerializado(instance, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def BorrarConsorcio(request, pk=None):
    member = Consorcio.objects.get(pk=pk)
    member.delete()
    return Response(status=status.HTTP_200_OK)

@api_view(['GET'])
def VerTodosLosFinanciadores(request):
    result = Financiador.objects.all()
    serializer = FinanciadorSerializado(result, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def CrearFinanciador(request):
    if request.method == 'POST':
        serializer = FinanciadorSerializado(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def CambiarFinanciador(request, pk=None):
    try:
        instance = Financiador.objects.get(pk=pk)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_404_NOT_FOUND)

    serializer = FinanciadorSerializado(instance, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def BorrarFinanciador(request, pk=None):
    member = Financiador.objects.get(pk=pk)
    member.delete()
    return Response(status=status.HTTP_200_OK)

@api_view(['GET'])
def VerTodosLosInstrumentos(request):
    result = Instrumento.objects.all()
    serializer = InstrumentoSerializado(result, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def CrearInstrumento(request):
    if request.method == 'POST':
        serializer = InstrumentoSerializado(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def CambiarInstrumento(request, pk=None):
    try:
        instance = Instrumento.objects.get(pk=pk)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_404_NOT_FOUND)

    serializer = InstrumentoSerializado(instance, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def BorrarInstrumento(request, pk=None):
    member = Instrumento.objects.get(pk=pk)
    member.delete()
    return Response(status=status.HTTP_200_OK)

@api_view(['GET'])
def VerTodasLasPostulaciones(request):
    result = Postulacion.objects.all()
    serializer = PostulacionSerializado(result, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def CrearPostulacion(request):
    if request.method == 'POST':
        serializer = PostulacionSerializado(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def CambiarPostulacion(request, pk=None):
    try:
        instance = Postulacion.objects.get(pk=pk)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_404_NOT_FOUND)

    serializer = PostulacionSerializado(instance, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def BorrarPostulacion(request, pk=None):
    member = Postulacion.objects.get(pk=pk)
    member.delete()
    return Response(status=status.HTTP_200_OK)
