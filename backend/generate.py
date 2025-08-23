import ast
import os
import re

SERIAL_FILE = "serializers.py"
MODELS_FILE = "models.py"
VIEWS_FILE = "views.py"
URLS_FILE = "urls.py"
ADMIN_FILE = "admin.py"
SEARCH_FILE = "search.py"
FORMS_FILE = "forms.py"
TEMP_DIR = "templates"

VOCALES = {
    'a', 'e', 'i', 'o', 'u',
    'A', 'E', 'I', 'O', 'U'
}

FORM_HTML = """<form method="post">
{% csrf_token %}
{{ form }}
<input type="submit" value="Submit">
</form>"""

SEARCH_HTML = """<form method="post">
{% csrf_token %}
{{ form }}
<input type="submit" value="Submit">
</form>"""

# Parsea models.py y devuelve una lista de clases modelo con sus campos, 
# omitiendo diccionarios definidos dentro de la clase
def parse_models(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        tree = ast.parse(f.read(), filename=file_path)

    models = []
    for node in tree.body:
        if isinstance(node, ast.ClassDef):
            for base in node.bases:
                if isinstance(base, ast.Attribute) and base.attr == "Model":
                    fields = []
                    for stmt in node.body:
                        if isinstance(stmt, ast.Assign):  
                            target = stmt.targets[0]
                            if isinstance(stmt.value, ast.Dict):
                                continue
                            if isinstance(target, ast.Name):
                                fields.append(target.id)
                    models.append((node.name, fields))
    return models

# Parsea models.py y devuelve una lista de clases modelo con sus campos y valores, 
# omitiendo diccionarios definidos dentro de la clase
def parse_models_with_value(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        tree = ast.parse(f.read(), filename=file_path)

    models = []
    for node in tree.body:
        if isinstance(node, ast.ClassDef):
            for base in node.bases:
                if isinstance(base, ast.Attribute) and base.attr == "Model":
                    fields = {}
                    for stmt in node.body:
                        if isinstance(stmt, ast.Assign):  
                            target = stmt.targets[0]
                            if isinstance(stmt.value, ast.Dict):
                                continue
                            if isinstance(target, ast.Name):
                                try:
                                    value = ast.unparse(stmt.value)
                                except AttributeError:
                                    value = str(stmt.value)
                                fields[target.id] = value
                    models.append((node.name, fields))
    return models

# Genera los serializadores por modelo para pasarlos en formato JSON
def generate_serializers(models):
    lines = [
        "from rest_framework import serializers",
        "from .models import *",
        "",
    ]
    for model, fields in models:
        lines.append(f"class {model}Serializado(serializers.ModelSerializer):")
        lines.append(f"    class Meta:")
        lines.append(f"        model = {model}")
        lines.append(f"        fields = {tuple(fields)}")
        lines.append(f"")
    return "\n".join(lines)

# Genera las vistas para leer, crear y modificar objetos del modelo
def generate_views(models):
    lines = [
        "from django.http import JsonResponse",
        "from django.db import connection",
        "from rest_framework.response import Response",
        "from rest_framework.decorators import api_view",
        "from rest_framework import status",
        "from .serializers import *",
        "from .models import *",
        "import requests",
        "import json",
        "from django.db.models import *",
        "",
    ]

    for model, _ in models:
        serializer = f"{model}Serializado"
        modelplural = str(model)
        todes = ""

        if modelplural[-1] == "a" or modelplural[-4:] == "cion":
            todes = "TodasLas"
        else:
            todes = "TodosLos"
        
        if modelplural[-1] in VOCALES:
            modelplural += "s"
        else:
            modelplural += "es"
        
        # GET
        lines.append(f"@api_view(['GET'])")
        lines.append(f"def Ver{todes}{modelplural}(request):")
        lines.append(f"    result = {model}.objects.all()")
        lines.append(f"    serializer = {serializer}(result, many=True)")
        lines.append(f"    return Response(serializer.data)")
        lines.append(f"")
        
        # POST
        lines.append(f"@api_view(['POST'])")
        lines.append(f"def Crear{model}(request):")
        lines.append(f"    if request.method == 'POST':")
        lines.append(f"        serializer = {serializer}(data=request.data)")
        lines.append(f"        if serializer.is_valid():")
        lines.append(f"            serializer.save()")
        lines.append(f"            return Response(serializer.data, status=status.HTTP_201_CREATED)")
        lines.append(f"    return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)")
        lines.append(f"")

        # PUT
        lines.append(f"@api_view(['PUT'])")
        lines.append(f"def Cambiar{model}(request, pk=None):")
        lines.append(f"    try:")
        lines.append(f"        instance = {model}.objects.get(pk=pk)")
        lines.append(f"    except Exception as e:")
        lines.append("        return Response({'error': str(e)}, status=status.HTTP_404_NOT_FOUND)")
        lines.append(f"")
        lines.append(f"    serializer = {serializer}(instance, data=request.data)")
        lines.append(f"    if serializer.is_valid():")
        lines.append(f"        serializer.save()")
        lines.append(f"        return Response(serializer.data)")
        lines.append(f"    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)")
        lines.append(f"")

    return "\n".join(lines)

# Genera el archivo admin para habilitar el acceso a los modelos
def generate_admin(models):
    lines = [
        "from django.contrib import admin",
        "from .models import *",
        ""
    ]
    for model, _ in models:
        lines.append(f"admin.site.register({model})")
    return "\n".join(lines)

# Genera formularios para crear objetos nuevos en base a los modelos
# Si existe una llave foranea, el formulario deja elegir el objeto en
# base a su nombre
def generate_forms(models):
    forms_code = [
        "from django.http import HttpResponseRedirect",
        "from django.shortcuts import render",
        "from django import forms",
        "from .models import *",
        "",
    ]
    for model, fields in models:
        formfields = tuple(fields)
        forms_code.append(f"class {model}Form(forms.ModelForm):")
        forms_code.append(f"    class Meta:")
        forms_code.append(f"        model = {model}")
        forms_code.append(f"        fields = {formfields}")
        forms_code.append("")
        forms_code.append(f"def VerFormulario{model}(request):")
        forms_code.append("    context = {}")
        forms_code.append(f"    if request.method == 'POST':")
        forms_code.append(f"        form = {model}Form(request.POST)")
        forms_code.append(f"        if form.is_valid():")
        forms_code.append(f"            obj = {model}(**form.cleaned_data)")
        forms_code.append(f"            obj.save()")
        forms_code.append(f"    if request.method == 'GET':")
        forms_code.append(f"        form = {model}Form()")
        for field in formfields:
            if field != "ID":
                forms_code.append(f"        context['{field.lower()}'] = '{field}'")
        forms_code.append(f"    return render(request, 'form.html', {{'form': form}})")
        forms_code.append("")
    
    with open(os.path.join("..", TEMP_DIR, f"form.html"), "w", encoding="utf-8") as f:
        f.write(FORM_HTML)

    with open(FORMS_FILE, "w", encoding="utf-8") as f:
        f.write("\n".join(forms_code))


# Genera APIs para buscar los modelos en base a campos de texto
def generate_search(models):
    forms_code = [
        "from rest_framework.response import Response",
        "from django.http import JsonResponse, HttpResponse, HttpResponseRedirect",
        "from django.views.decorators.csrf import csrf_exempt",
        "from django.template import Template, Context",
        "from django.shortcuts import render",
        "from django import forms",
        "from .serializers import *",
        "from .models import *"
        "\n",
        "SEARCH_TEMPLATE = '''",
        "<!DOCTYPE html>",
        "<html>",
        "<head>",
        "    <title>Busqueda por texto</title>",
        "</head>",
        "<body>",
        "    <form method=\"post\">",
        "        {% csrf_token %}",
        "        <input type=\"text\" name=\"q\" required>",
        "        <button type=\"submit\">Buscar</button>",
        "    </form>",
        "</body>",
        "</html>",
        "'''",
        ""
    ]
    for model, fields in models:
        if "RUT" in fields:
            forms_code.append(f"@csrf_exempt")
            forms_code.append(f"def Buscar{model}PorRUT(request):")
            forms_code.append(f"    if request.method == \"GET\":")
            forms_code.append(f"        tmpl = Template(SEARCH_TEMPLATE)")
            forms_code.append("        html = tmpl.render(Context({}))")
            forms_code.append(f"        return HttpResponse(html)")
            forms_code.append(f"    elif request.method == \"POST\":")
            forms_code.append(f"        query = request.POST.get(\"q\", "")")
            forms_code.append(f"        if not query:")
            forms_code.append("            return JsonResponse({\"error\": \"Debe ingresar un término de búsqueda\"}, status=400)")
            forms_code.append(f"        result = {model}.objects.filter(RUT__iregex=query) | {model}.objects.filter(RUT__icontains=query)")
            forms_code.append(f"        serializer = {model}Serializado(result, many=True)")
            forms_code.append(f"        return JsonResponse(serializer.data, safe=False)")
            forms_code.append("")

        if "Nombre" in fields:
            forms_code.append(f"@csrf_exempt")
            forms_code.append(f"def Buscar{model}PorNombre(request):")
            forms_code.append(f"    if request.method == \"GET\":")
            forms_code.append(f"        tmpl = Template(SEARCH_TEMPLATE)")
            forms_code.append("        html = tmpl.render(Context({}))")
            forms_code.append(f"        return HttpResponse(html)")
            forms_code.append(f"    elif request.method == \"POST\":")
            forms_code.append(f"        query = request.POST.get(\"q\", "")")
            forms_code.append(f"        if not query:")
            forms_code.append("            return JsonResponse({\"error\": \"Debe ingresar un término de búsqueda\"}, status=400)")
            forms_code.append(f"        result = {model}.objects.filter(Nombre__iregex=query) | {model}.objects.filter(Nombre__icontains=query)")
            forms_code.append(f"        serializer = {model}Serializado(result, many=True)")
            forms_code.append(f"        return JsonResponse(serializer.data, safe=False)")
            forms_code.append("")

        elif "Titulo" in fields:
            forms_code.append(f"@csrf_exempt")
            forms_code.append(f"def Buscar{model}PorTitulo(request):")
            forms_code.append(f"    if request.method == \"GET\":")
            forms_code.append(f"        tmpl = Template(SEARCH_TEMPLATE)")
            forms_code.append("        html = tmpl.render(Context({}))")
            forms_code.append(f"        return HttpResponse(html)")
            forms_code.append(f"    elif request.method == \"POST\":")
            forms_code.append(f"        query = request.POST.get(\"q\", "")")
            forms_code.append(f"        if not query:")
            forms_code.append("            return JsonResponse({\"error\": \"Debe ingresar un término de búsqueda\"}, status=400)")
            forms_code.append(f"        result = {model}.objects.filter(Titulo__iregex=query) | {model}.objects.filter(Titulo__icontains=query)")
            forms_code.append(f"        serializer = {model}Serializado(result, many=True)")
            forms_code.append(f"        return JsonResponse(serializer.data, safe=False)")
            forms_code.append("")

    with open(os.path.join("..", TEMP_DIR, f"search.html"), "w", encoding="utf-8") as f:
        f.write(SEARCH_HTML)

    with open(SEARCH_FILE, "w", encoding="utf-8") as f:
        f.write("\n".join(forms_code))

# Genera los endpoint para las APIs
def generate_urls(models):
    lines = [
        "from django.contrib import admin",
        "from django.urls import path",
        "from . import views",
        "from . import forms",
        "from . import search",
        "",
        "urlpatterns = [",
        "    path('admin/', admin.site.urls),",
    ]
    for model, _ in models:
        modelplural = str(model)
        todes = ""
        if modelplural[-1] == "a" or modelplural[-4:] == "cion":
            todes = "TodasLas"
        else:
            todes = "TodosLos"
        if modelplural[-1] in VOCALES:
            modelplural += "s"
        else:
            modelplural += "es"
        lines.append(f"    path('ver{todes.lower()}{modelplural.lower()}/', views.Ver{todes}{modelplural}),")
        
    for model, _ in models:
        lines.append(f"    path('crear{model.lower()}/', views.Crear{model}),")
        
    for model, _ in models:
        lines.append(f"    path('cambiar{model.lower()}/<int:pk>/', views.Cambiar{model}),")
        
    for model, _ in models:
        lines.append(f"    path('formulario{model.lower()}/', forms.VerFormulario{model}),")
    
    for model, fields in models:
        if "RUT" in fields:
            lines.append(f"    path('buscar{model.lower()}porrut/', search.Buscar{model}PorRUT),")
        if "Nombre" in fields:
            lines.append(f"    path('buscar{model.lower()}pornombre/', search.Buscar{model}PorNombre),")
        elif "Titulo" in fields:
            lines.append(f"    path('buscar{model.lower()}portitulo/', search.Buscar{model}PorTitulo),")
    
    lines.append("]")
    return "\n".join(lines)


def main():
    models = parse_models(MODELS_FILE)

    with open(SERIAL_FILE, "w", encoding="utf-8") as f:
        f.write(generate_serializers(models))

    with open(VIEWS_FILE, "w", encoding="utf-8") as f:
        f.write(generate_views(models))

    with open(URLS_FILE, "w", encoding="utf-8") as f:
        f.write(generate_urls(models))

    with open(ADMIN_FILE, "w", encoding="utf-8") as f:
        f.write(generate_admin(models))

    models = parse_models_with_value(MODELS_FILE)
    generate_forms(models)

    models = parse_models_with_value(MODELS_FILE)
    generate_search(models)

    print("Archivos generados correctamente!")


if __name__ == "__main__":
    main()
