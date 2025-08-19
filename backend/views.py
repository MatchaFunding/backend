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
def LeerUbicacion(request):
    result = Ubicacion.objects.all()
    serializer = UbicacionSerializado(result, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def CrearUbicacion(request):
    if request.method == 'POST':
        serializer = UbicacionSerializado(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def CambiarUbicacion(request, pk=None):
    try:
        instance = Ubicacion.objects.get(pk=pk)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_404_NOT_FOUND)

    serializer = UbicacionSerializado(instance, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def LeerBeneficiario(request):
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

@api_view(['GET'])
def LeerProyecto(request):
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

@api_view(['GET'])
def LeerPersona(request):
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

@api_view(['GET'])
def LeerMiembroDeUnaEmpresa(request):
    result = MiembroDeUnaEmpresa.objects.all()
    serializer = MiembroDeUnaEmpresaSerializado(result, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def CrearMiembroDeUnaEmpresa(request):
    if request.method == 'POST':
        serializer = MiembroDeUnaEmpresaSerializado(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def CambiarMiembroDeUnaEmpresa(request, pk=None):
    try:
        instance = MiembroDeUnaEmpresa.objects.get(pk=pk)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_404_NOT_FOUND)

    serializer = MiembroDeUnaEmpresaSerializado(instance, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def LeerMiembroDeProyecto(request):
    result = MiembroDeProyecto.objects.all()
    serializer = MiembroDeProyectoSerializado(result, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def CrearMiembroDeProyecto(request):
    if request.method == 'POST':
        serializer = MiembroDeProyectoSerializado(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def CambiarMiembroDeProyecto(request, pk=None):
    try:
        instance = MiembroDeProyecto.objects.get(pk=pk)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_404_NOT_FOUND)

    serializer = MiembroDeProyectoSerializado(instance, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def LeerUsuarioDeMatchaFunding(request):
    result = UsuarioDeMatchaFunding.objects.all()
    serializer = UsuarioDeMatchaFundingSerializado(result, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def CrearUsuarioDeMatchaFunding(request):
    if request.method == 'POST':
        serializer = UsuarioDeMatchaFundingSerializado(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def CambiarUsuarioDeMatchaFunding(request, pk=None):
    try:
        instance = UsuarioDeMatchaFunding.objects.get(pk=pk)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_404_NOT_FOUND)

    serializer = UsuarioDeMatchaFundingSerializado(instance, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def LeerConsorcioDeBeneficiarios(request):
    result = ConsorcioDeBeneficiarios.objects.all()
    serializer = ConsorcioDeBeneficiariosSerializado(result, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def CrearConsorcioDeBeneficiarios(request):
    if request.method == 'POST':
        serializer = ConsorcioDeBeneficiariosSerializado(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def CambiarConsorcioDeBeneficiarios(request, pk=None):
    try:
        instance = ConsorcioDeBeneficiarios.objects.get(pk=pk)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_404_NOT_FOUND)

    serializer = ConsorcioDeBeneficiariosSerializado(instance, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def LeerFinanciador(request):
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

@api_view(['GET'])
def LeerInstrumento(request):
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

@api_view(['GET'])
def LeerPostulacion(request):
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
