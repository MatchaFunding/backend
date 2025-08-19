import ast
import os

MODELS_FILE = "models.py"
SERIALIZERS_FILE = "serializers.py"
VIEWS_FILE = "views.py"
URLS_FILE = "urls.py"


def parse_models(file_path):
    """Parsea models.py y devuelve una lista de clases modelo con sus campos"""
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
                            if isinstance(stmt.targets[0], ast.Name):
                                fields.append(stmt.targets[0].id)
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
        lines.append("    class Meta:")
        lines.append(f"        model = {model}")
        lines.append(f"        fields = {tuple(fields)}")
        lines.append("")
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

        # GET
        lines.append("@api_view(['GET'])")
        lines.append(f"def Ver{model}s(request):")
        lines.append(f"    result = {model}.objects.all()")
        lines.append(f"    serializer = {serializer}(result, many=True)")
        lines.append("    return Response(serializer.data)")
        lines.append("")

        # POST
        lines.append("@api_view(['POST'])")
        lines.append(f"def Crear{model}(request):")
        lines.append("    if request.method == 'POST':")
        lines.append(f"        serializer = {serializer}(data=request.data)")
        lines.append("        if serializer.is_valid():")
        lines.append("            serializer.save()")
        lines.append("            return Response(serializer.data, status=status.HTTP_201_CREATED)")
        lines.append("    return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)")
        lines.append("")

        # PUT
        lines.append("@api_view(['PUT'])")
        lines.append(f"def Modificar{model}(request, pk=None):")
        lines.append(f"    try:")
        lines.append(f"        instance = {model}.objects.get(pk=pk)")
        lines.append("    except Exception as e:")
        lines.append("        return Response({'error': str(e)}, status=status.HTTP_404_NOT_FOUND)")
        lines.append("")
        lines.append(f"    serializer = {serializer}(instance, data=request.data)")
        lines.append("    if serializer.is_valid():")
        lines.append("        serializer.save()")
        lines.append("        return Response(serializer.data)")
        lines.append("    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)")
        lines.append("")

    return "\n".join(lines)


def generate_urls(models):
    lines = [
        "from django.contrib import admin",
        "from django.urls import path",
        "from . import views",
        "",
        "urlpatterns = [",
        "    path('admin/', admin.site.urls),",
    ]
    for model, _ in models:
        lines.append(f"    path('ver{model.lower()}s/', views.Ver{model}s),")
        lines.append(f"    path('crear{model.lower()}/', views.Crear{model}),")
        lines.append(f"    path('modificar{model.lower()}/<int:pk>/', views.Modificar{model}),")
    lines.append("]")
    return "\n".join(lines)


def main():
    models = parse_models(MODELS_FILE)

    with open(SERIALIZERS_FILE, "w", encoding="utf-8") as f:
        f.write(generate_serializers(models))

    with open(VIEWS_FILE, "w", encoding="utf-8") as f:
        f.write(generate_views(models))

    with open(URLS_FILE, "w", encoding="utf-8") as f:
        f.write(generate_urls(models))

    print("Archivos serializers.py, views.py y urls.py generados correctamente.")


if __name__ == "__main__":
    main()
