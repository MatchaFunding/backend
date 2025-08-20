import ast
import os
import re

SERIAL_FILE = "serializers.py"
MODELS_FILE = "models.py"
VIEWS_FILE = "views.py"
URLS_FILE = "urls.py"
ADMIN_FILE = "admin.py"
FORMS_FILE = "forms.py"
FORMS_DIR = "templates"

VOCALES = {
    'a', 'e', 'i', 'o', 'u',
    'A', 'E', 'I', 'O', 'U'
}

def parse_models(file_path):
    """Parsea models.py y devuelve una lista de clases modelo con sus campos, 
    omitiendo diccionarios definidos dentro de la clase"""
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


def parse_models_with_value(file_path):
    """Parsea models.py y devuelve una lista de clases modelo con sus campos y valores, 
    omitiendo diccionarios definidos dentro de la clase"""
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


def generate_urls(models):
    lines = [
        "from django.contrib import admin",
        "from django.urls import path",
        "from . import views",
        "from . import forms",
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
        lines.append(f"    path('crear{model.lower()}/', views.Crear{model}),")
        lines.append(f"    path('cambiar{model.lower()}/<int:pk>/', views.Cambiar{model}),")
        lines.append(f"    path('formulario{model.lower()}/', forms.Formulario{model}),")
    lines.append("]")
    return "\n".join(lines)


def generate_admin(models):
    lines = [
        "from django.contrib import admin",
        "from .models import *",
        ""
    ]
    for model, _ in models:
        lines.append(f"admin.site.register({model})")
    return "\n".join(lines)


def generate_forms(models):
    forms_code = [
        "from django.http import HttpResponseRedirect",
        "from django.shortcuts import render",
        "from django import forms",
        "from .models import *",
        "",
    ]
    for model, fields in models:
        class_name = f"{model}Form"
        forms_code.append(f"class {class_name}(forms.Form):")
        
        for field in fields.items():
            name = field[0]
            value = field[1].replace("models", "forms")
            value = field[1].replace("BigAutoField(primary_key=True)", "IntegerField()")
            value = re.sub("ForeignKey\([a-zA-Z\,\.\ _=]*\)", "IntegerField()", value)
            value = re.sub(", choices=[A-Z]*", "", value)
            forms_code.append(f"    {name} = {value}")
        
        forms_code.append("")
        func_name = f"Formulario{model}"
        forms_code.append(f"def {func_name}(request):")
        forms_code.append(f"    if request.method == 'POST':")
        forms_code.append(f"        form = {class_name}(request.POST)")
        forms_code.append(f"        if form.is_valid():")
        forms_code.append(f"            obj = {model}(**form.cleaned_data)")
        forms_code.append(f"            obj.save()")
        forms_code.append(f"            return HttpResponseRedirect('/thanks/')")
        forms_code.append(f"    else:")
        forms_code.append(f"        form = {class_name}()")
        forms_code.append(f"    return render(request, '{model.lower()}.html', {{'form': form}})")
        forms_code.append("")
        html_code = """
<form method="post">
    {% csrf_token %}
    {{ form }}
    <input type="submit" value="Submit">
</form>"""
        with open(os.path.join("..", FORMS_DIR, f"{model.lower()}.html"), "w", encoding="utf-8") as f:
            f.write(html_code)

    with open(FORMS_FILE, "w", encoding="utf-8") as f:
        f.write("\n".join(forms_code))


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

    print("Archivos generados correctamente!")


if __name__ == "__main__":
    main()
