from rest_framework.response import Response
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django import forms
from .serializers import *
from .models import *

from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.template import Template, Context

class UbicacionBusqueda(forms.ModelForm):
    class Meta:
        model = Ubicacion
        fields = ('ID', 'Region', 'Capital', 'Calle', 'Numero')

def VerBusquedaUbicacion(request):
    context = {}
    result = Ubicacion.objects.all()
    serializer = UbicacionSerializado(result, many=True)
    response = Response(serializer.data)
    if request.method == 'POST':
        form = UbicacionBusqueda(request.POST)
        print(f'Resultado de busqueda: {serializer.data}')
    if request.method == 'GET':
        form = UbicacionBusqueda()
        context['region'] = 'Region'
        context['capital'] = 'Capital'
        context['calle'] = 'Calle'
        context['numero'] = 'Numero'
    return render(request, 'search.html', {'form': form})

class BeneficiarioBusqueda(forms.ModelForm):
    class Meta:
        model = Beneficiario
        fields = ('ID', 'Nombre', 'FechaDeCreacion', 'LugarDeCreacion', 'TipoDePersona', 'TipoDeEmpresa', 'Perfil', 'RUTdeEmpresa', 'RUTdeRepresentante')

SEARCH_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Búsqueda de Beneficiarios</title>
</head>
<body>
    <form method="post">
        {% csrf_token %}
        <input type="text" name="q" placeholder="Nombre del beneficiario" required>
        <button type="submit">Buscar</button>
    </form>
</body>
</html>
"""
@csrf_exempt
def VerBusquedaBeneficiario(request):
    if request.method == "GET":
        tmpl = Template(SEARCH_TEMPLATE)
        html = tmpl.render(Context({}))
        return HttpResponse(html)
    elif request.method == "POST":
        query = request.POST.get("q", "")
        if not query:
            return JsonResponse({"error": "Debe ingresar un término de búsqueda"}, status=400)
        result = Beneficiario.objects.filter(Nombre__iregex=query) | Beneficiario.objects.filter(Nombre__icontains=query)
        serializer = BeneficiarioSerializado(result, many=True)
        return JsonResponse(serializer.data, safe=False)

class ProyectoBusqueda(forms.ModelForm):
    class Meta:
        model = Proyecto
        fields = ('ID', 'Beneficiario', 'Titulo', 'Descripcion', 'DuracionEnMesesMinimo', 'DuracionEnMesesMaximo', 'Alcance', 'Area')

def VerBusquedaProyecto(request):
    context = {}
    result = Proyecto.objects.all()
    serializer = ProyectoSerializado(result, many=True)
    response = Response(serializer.data)
    if request.method == 'POST':
        form = ProyectoBusqueda(request.POST)
        print(f'Resultado de busqueda: {serializer.data}')
    if request.method == 'GET':
        form = ProyectoBusqueda()
        context['beneficiario'] = 'Beneficiario'
        context['titulo'] = 'Titulo'
        context['descripcion'] = 'Descripcion'
        context['duracionenmesesminimo'] = 'DuracionEnMesesMinimo'
        context['duracionenmesesmaximo'] = 'DuracionEnMesesMaximo'
        context['alcance'] = 'Alcance'
        context['area'] = 'Area'
    return render(request, 'search.html', {'form': form})

class PersonaBusqueda(forms.ModelForm):
    class Meta:
        model = Persona
        fields = ('ID', 'Nombre', 'Sexo', 'RUT')

def VerBusquedaPersona(request):
    context = {}
    result = Persona.objects.all()
    serializer = PersonaSerializado(result, many=True)
    response = Response(serializer.data)
    if request.method == 'POST':
        form = PersonaBusqueda(request.POST)
        print(f'Resultado de busqueda: {serializer.data}')
    if request.method == 'GET':
        form = PersonaBusqueda()
        context['nombre'] = 'Nombre'
        context['sexo'] = 'Sexo'
        context['rut'] = 'RUT'
    return render(request, 'search.html', {'form': form})

class MiembroBusqueda(forms.ModelForm):
    class Meta:
        model = Miembro
        fields = ('ID', 'Persona', 'Beneficiario')

def VerBusquedaMiembro(request):
    context = {}
    result = Miembro.objects.all()
    serializer = MiembroSerializado(result, many=True)
    response = Response(serializer.data)
    if request.method == 'POST':
        form = MiembroBusqueda(request.POST)
        print(f'Resultado de busqueda: {serializer.data}')
    if request.method == 'GET':
        form = MiembroBusqueda()
        context['persona'] = 'Persona'
        context['beneficiario'] = 'Beneficiario'
    return render(request, 'search.html', {'form': form})

class ColaboradorBusqueda(forms.ModelForm):
    class Meta:
        model = Colaborador
        fields = ('ID', 'Persona', 'Proyecto')

def VerBusquedaColaborador(request):
    context = {}
    result = Colaborador.objects.all()
    serializer = ColaboradorSerializado(result, many=True)
    response = Response(serializer.data)
    if request.method == 'POST':
        form = ColaboradorBusqueda(request.POST)
        print(f'Resultado de busqueda: {serializer.data}')
    if request.method == 'GET':
        form = ColaboradorBusqueda()
        context['persona'] = 'Persona'
        context['proyecto'] = 'Proyecto'
    return render(request, 'search.html', {'form': form})

class UsuarioBusqueda(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ('ID', 'Persona', 'NombreDeUsuario', 'Contrasena', 'Correo')

def VerBusquedaUsuario(request):
    context = {}
    result = Usuario.objects.all()
    serializer = UsuarioSerializado(result, many=True)
    response = Response(serializer.data)
    if request.method == 'POST':
        form = UsuarioBusqueda(request.POST)
        print(f'Resultado de busqueda: {serializer.data}')
    if request.method == 'GET':
        form = UsuarioBusqueda()
        context['persona'] = 'Persona'
        context['nombredeusuario'] = 'NombreDeUsuario'
        context['contrasena'] = 'Contrasena'
        context['correo'] = 'Correo'
    return render(request, 'search.html', {'form': form})

class ConsorcioBusqueda(forms.ModelForm):
    class Meta:
        model = Consorcio
        fields = ('ID', 'PrimerBeneficiario', 'SegundoBeneficiario')

def VerBusquedaConsorcio(request):
    context = {}
    result = Consorcio.objects.all()
    serializer = ConsorcioSerializado(result, many=True)
    response = Response(serializer.data)
    if request.method == 'POST':
        form = ConsorcioBusqueda(request.POST)
        print(f'Resultado de busqueda: {serializer.data}')
    if request.method == 'GET':
        form = ConsorcioBusqueda()
        context['primerbeneficiario'] = 'PrimerBeneficiario'
        context['segundobeneficiario'] = 'SegundoBeneficiario'
    return render(request, 'search.html', {'form': form})

class FinanciadorBusqueda(forms.ModelForm):
    class Meta:
        model = Financiador
        fields = ('ID', 'Nombre', 'FechaDeCreacion', 'LugarDeCreacion', 'TipoDePersona', 'TipoDeEmpresa', 'Perfil', 'RUTdeEmpresa', 'RUTdeRepresentante')

def VerBusquedaFinanciador(request):
    context = {}
    result = Financiador.objects.all()
    serializer = FinanciadorSerializado(result, many=True)
    response = Response(serializer.data)
    if request.method == 'POST':
        form = FinanciadorBusqueda(request.POST)
        print(f'Resultado de busqueda: {serializer.data}')
    if request.method == 'GET':
        form = FinanciadorBusqueda()
        context['nombre'] = 'Nombre'
        context['fechadecreacion'] = 'FechaDeCreacion'
        context['lugardecreacion'] = 'LugarDeCreacion'
        context['tipodepersona'] = 'TipoDePersona'
        context['tipodeempresa'] = 'TipoDeEmpresa'
        context['perfil'] = 'Perfil'
        context['rutdeempresa'] = 'RUTdeEmpresa'
        context['rutderepresentante'] = 'RUTdeRepresentante'
    return render(request, 'search.html', {'form': form})

class InstrumentoBusqueda(forms.ModelForm):
    class Meta:
        model = Instrumento
        fields = ('ID', 'Titulo', 'Financiador', 'Alcance', 'Descripcion', 'FechaDeApertura', 'FechaDeCierre', 'DuracionEnMeses', 'Beneficios', 'Requisitos', 'MontoMinimo', 'MontoMaximo', 'Estado', 'TipoDeBeneficio', 'TipoDePerfil', 'EnlaceDelDetalle', 'EnlaceDeLaFoto')

def VerBusquedaInstrumento(request):
    context = {}
    result = Instrumento.objects.all()
    serializer = InstrumentoSerializado(result, many=True)
    response = Response(serializer.data)
    if request.method == 'POST':
        form = InstrumentoBusqueda(request.POST)
        print(f'Resultado de busqueda: {serializer.data}')
    if request.method == 'GET':
        form = InstrumentoBusqueda()
        context['titulo'] = 'Titulo'
        context['financiador'] = 'Financiador'
        context['alcance'] = 'Alcance'
        context['descripcion'] = 'Descripcion'
        context['fechadeapertura'] = 'FechaDeApertura'
        context['fechadecierre'] = 'FechaDeCierre'
        context['duracionenmeses'] = 'DuracionEnMeses'
        context['beneficios'] = 'Beneficios'
        context['requisitos'] = 'Requisitos'
        context['montominimo'] = 'MontoMinimo'
        context['montomaximo'] = 'MontoMaximo'
        context['estado'] = 'Estado'
        context['tipodebeneficio'] = 'TipoDeBeneficio'
        context['tipodeperfil'] = 'TipoDePerfil'
        context['enlacedeldetalle'] = 'EnlaceDelDetalle'
        context['enlacedelafoto'] = 'EnlaceDeLaFoto'
    return render(request, 'search.html', {'form': form})

class PostulacionBusqueda(forms.ModelForm):
    class Meta:
        model = Postulacion
        fields = ('ID', 'Beneficiario', 'Proyecto', 'Instrumento', 'Resultado', 'MontoObtenido', 'FechaDePostulacion', 'FechaDeResultado', 'Detalle')

def VerBusquedaPostulacion(request):
    context = {}
    result = Postulacion.objects.all()
    serializer = PostulacionSerializado(result, many=True)
    response = Response(serializer.data)
    if request.method == 'POST':
        form = PostulacionBusqueda(request.POST)
        print(f'Resultado de busqueda: {serializer.data}')
    if request.method == 'GET':
        form = PostulacionBusqueda()
        context['beneficiario'] = 'Beneficiario'
        context['proyecto'] = 'Proyecto'
        context['instrumento'] = 'Instrumento'
        context['resultado'] = 'Resultado'
        context['montoobtenido'] = 'MontoObtenido'
        context['fechadepostulacion'] = 'FechaDePostulacion'
        context['fechaderesultado'] = 'FechaDeResultado'
        context['detalle'] = 'Detalle'
    return render(request, 'search.html', {'form': form})
