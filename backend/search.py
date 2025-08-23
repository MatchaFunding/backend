from rest_framework.response import Response
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.template import Template, Context
from django.shortcuts import render
from django import forms
from .serializers import *
from .models import *

SEARCH_TEMPLATE = '''
<!DOCTYPE html>
<html>
<head>
    <title>Busqueda por texto</title>
</head>
<body>
    <form method="post">
        {% csrf_token %}
        <input type="text" name="q" required>
        <button type="submit">Buscar</button>
    </form>
</body>
</html>
'''

@csrf_exempt
def BuscarBeneficiario(request):
    if request.method == "GET":
        tmpl = Template(SEARCH_TEMPLATE)
        html = tmpl.render(Context({}))
        return HttpResponse(html)
    elif request.method == "POST":
        query = request.POST.get("q", )
        if not query:
            return JsonResponse({"error": "Debe ingresar un término de búsqueda"}, status=400)
        result = Beneficiario.objects.filter(Nombre__iregex=query) | Beneficiario.objects.filter(Nombre__icontains=query)
        serializer = BeneficiarioSerializado(result, many=True)
        return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def BuscarProyecto(request):
    if request.method == "GET":
        tmpl = Template(SEARCH_TEMPLATE)
        html = tmpl.render(Context({}))
        return HttpResponse(html)
    elif request.method == "POST":
        query = request.POST.get("q", )
        if not query:
            return JsonResponse({"error": "Debe ingresar un término de búsqueda"}, status=400)
        result = Proyecto.objects.filter(Titulo__iregex=query) | Proyecto.objects.filter(Titulo__icontains=query)
        serializer = ProyectoSerializado(result, many=True)
        return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def BuscarPersona(request):
    if request.method == "GET":
        tmpl = Template(SEARCH_TEMPLATE)
        html = tmpl.render(Context({}))
        return HttpResponse(html)
    elif request.method == "POST":
        query = request.POST.get("q", )
        if not query:
            return JsonResponse({"error": "Debe ingresar un término de búsqueda"}, status=400)
        result = Persona.objects.filter(RUT__iregex=query) | Persona.objects.filter(RUT__icontains=query) | Persona.objects.filter(Nombre__iregex=query) | Persona.objects.filter(Nombre__icontains=query)
        serializer = PersonaSerializado(result, many=True)
        return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def BuscarFinanciador(request):
    if request.method == "GET":
        tmpl = Template(SEARCH_TEMPLATE)
        html = tmpl.render(Context({}))
        return HttpResponse(html)
    elif request.method == "POST":
        query = request.POST.get("q", )
        if not query:
            return JsonResponse({"error": "Debe ingresar un término de búsqueda"}, status=400)
        result = Financiador.objects.filter(Nombre__iregex=query) | Financiador.objects.filter(Nombre__icontains=query)
        serializer = FinanciadorSerializado(result, many=True)
        return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def BuscarInstrumento(request):
    if request.method == "GET":
        tmpl = Template(SEARCH_TEMPLATE)
        html = tmpl.render(Context({}))
        return HttpResponse(html)
    elif request.method == "POST":
        query = request.POST.get("q", )
        if not query:
            return JsonResponse({"error": "Debe ingresar un término de búsqueda"}, status=400)
        result = Instrumento.objects.filter(Titulo__iregex=query) | Instrumento.objects.filter(Titulo__icontains=query)
        serializer = InstrumentoSerializado(result, many=True)
        return JsonResponse(serializer.data, safe=False)
