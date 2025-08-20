from django.http import HttpResponseRedirect
from django.shortcuts import render
from django import forms
from .models import *

class UbicacionForm(forms.Form):
    ID = models.IntegerField()
    Region = models.CharField(max_length=30)
    Capital = models.CharField(max_length=30)
    Calle = models.CharField(max_length=300)
    Numero = models.IntegerField()

def FormularioUbicacion(request):
    if request.method == 'POST':
        form = UbicacionForm(request.POST)
        if form.is_valid():
            obj = Ubicacion(**form.cleaned_data)
            obj.save()
            return HttpResponseRedirect('/thanks/')
    else:
        form = UbicacionForm()
    return render(request, 'ubicacion.html', {'form': form})

class BeneficiarioForm(forms.Form):
    ID = models.IntegerField()
    Nombre = models.CharField(max_length=100)
    FechaDeCreacion = models.DateField()
    LugarDeCreacion = models.IntegerField()
    TipoDePersona = models.CharField(max_length=30)
    TipoDeEmpresa = models.CharField(max_length=30)
    Perfil = models.CharField(max_length=30)
    RUTdeEmpresa = models.CharField(max_length=12)
    RUTdeRepresentante = models.CharField(max_length=12)

def FormularioBeneficiario(request):
    if request.method == 'POST':
        form = BeneficiarioForm(request.POST)
        if form.is_valid():
            obj = Beneficiario(**form.cleaned_data)
            obj.save()
            return HttpResponseRedirect('/thanks/')
    else:
        form = BeneficiarioForm()
    return render(request, 'beneficiario.html', {'form': form})

class ProyectoForm(forms.Form):
    ID = models.IntegerField()
    Beneficiario = models.IntegerField()
    Titulo = models.CharField(max_length=300)
    Descripcion = models.CharField(max_length=500)
    DuracionEnMesesMinimo = models.IntegerField()
    DuracionEnMesesMaximo = models.IntegerField()
    Alcance = models.IntegerField()
    Area = models.CharField(max_length=100)

def FormularioProyecto(request):
    if request.method == 'POST':
        form = ProyectoForm(request.POST)
        if form.is_valid():
            obj = Proyecto(**form.cleaned_data)
            obj.save()
            return HttpResponseRedirect('/thanks/')
    else:
        form = ProyectoForm()
    return render(request, 'proyecto.html', {'form': form})

class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = ('ID', 'Nombre', 'Sexo', 'RUT')

def FormularioPersona(request):
    context = {}
    if request.method == 'POST':
        form = PersonaForm(request.POST)
        if form.is_valid():
            obj = Persona(**form.cleaned_data)
            obj.save()
            return HttpResponseRedirect('/thanks/')
    if request.method == 'GET':
        form = PersonaForm()
        context['nombre'] = "Nombre"
        context['sexo'] = "Sexo"
        context['rut'] = "RUT"
    return render(request, 'persona.html', {'form': form})

class MiembroForm(forms.Form):
    ID = models.IntegerField()
    Persona = models.IntegerField()
    Beneficiario = models.IntegerField()

def FormularioMiembro(request):
    if request.method == 'POST':
        form = MiembroForm(request.POST)
        if form.is_valid():
            obj = Miembro(**form.cleaned_data)
            obj.save()
            return HttpResponseRedirect('/thanks/')
    else:
        form = MiembroForm()
    return render(request, 'miembro.html', {'form': form})

class ColaboradorForm(forms.Form):
    ID = models.IntegerField()
    Persona = models.IntegerField()
    Proyecto = models.IntegerField()

def FormularioColaborador(request):
    if request.method == 'POST':
        form = ColaboradorForm(request.POST)
        if form.is_valid():
            obj = Colaborador(**form.cleaned_data)
            obj.save()
            return HttpResponseRedirect('/thanks/')
    else:
        form = ColaboradorForm()
    return render(request, 'colaborador.html', {'form': form})

class UsuarioForm(forms.Form):
    ID = models.IntegerField()
    Persona = models.IntegerField()
    NombreDeUsuario = models.CharField(max_length=200, null=False)
    Contrasena = models.CharField(max_length=200, null=False)
    Correo = models.CharField(max_length=200, null=False)

def FormularioUsuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            obj = Usuario(**form.cleaned_data)
            obj.save()
            return HttpResponseRedirect('/thanks/')
    else:
        form = UsuarioForm()
    return render(request, 'usuario.html', {'form': form})

class ConsorcioForm(forms.Form):
    ID = models.IntegerField()
    PrimerBeneficiario = models.ForeignKey(Beneficiario, on_delete=models.CASCADE, related_name='primero')
    SegundoBeneficiario = models.ForeignKey(Beneficiario, on_delete=models.CASCADE, related_name='segundo')

def FormularioConsorcio(request):
    if request.method == 'POST':
        form = ConsorcioForm(request.POST)
        if form.is_valid():
            obj = Consorcio(**form.cleaned_data)
            obj.save()
            return HttpResponseRedirect('/thanks/')
    else:
        form = ConsorcioForm()
    return render(request, 'consorcio.html', {'form': form})

class FinanciadorForm(forms.Form):
    ID = models.IntegerField()
    Nombre = models.CharField(max_length=100)
    FechaDeCreacion = models.DateField()
    LugarDeCreacion = models.IntegerField()
    TipoDePersona = models.CharField(max_length=30)
    TipoDeEmpresa = models.CharField(max_length=30)
    Perfil = models.CharField(max_length=30)
    RUTdeEmpresa = models.CharField(max_length=12)
    RUTdeRepresentante = models.CharField(max_length=12)

def FormularioFinanciador(request):
    if request.method == 'POST':
        form = FinanciadorForm(request.POST)
        if form.is_valid():
            obj = Financiador(**form.cleaned_data)
            obj.save()
            return HttpResponseRedirect('/thanks/')
    else:
        form = FinanciadorForm()
    return render(request, 'financiador.html', {'form': form})

class InstrumentoForm(forms.Form):
    ID = models.IntegerField()
    Titulo = models.CharField(max_length=200)
    Financiador = models.IntegerField()
    Alcance = models.IntegerField()
    Descripcion = models.CharField(max_length=1000)
    FechaDeApertura = models.DateField()
    FechaDeCierre = models.DateField()
    DuracionEnMeses = models.IntegerField()
    Beneficios = models.CharField(max_length=1000)
    Requisitos = models.CharField(max_length=1000)
    MontoMinimo = models.IntegerField()
    MontoMaximo = models.IntegerField()
    Estado = models.CharField(max_length=30)
    TipoDeBeneficio = models.CharField(max_length=30)
    TipoDePerfil = models.CharField(max_length=30)
    EnlaceDelDetalle = models.CharField(max_length=300)
    EnlaceDeLaFoto = models.CharField(max_length=300)

def FormularioInstrumento(request):
    if request.method == 'POST':
        form = InstrumentoForm(request.POST)
        if form.is_valid():
            obj = Instrumento(**form.cleaned_data)
            obj.save()
            return HttpResponseRedirect('/thanks/')
    else:
        form = InstrumentoForm()
    return render(request, 'instrumento.html', {'form': form})

class PostulacionForm(forms.Form):
    ID = models.IntegerField()
    Beneficiario = models.IntegerField()
    Proyecto = models.IntegerField()
    Instrumento = models.IntegerField()
    Resultado = models.CharField(max_length=30)
    MontoObtenido = models.IntegerField()
    FechaDePostulacion = models.DateField()
    FechaDeResultado = models.DateField()
    Detalle = models.CharField(max_length=1000)

def FormularioPostulacion(request):
    if request.method == 'POST':
        form = PostulacionForm(request.POST)
        if form.is_valid():
            obj = Postulacion(**form.cleaned_data)
            obj.save()
            return HttpResponseRedirect('/thanks/')
    else:
        form = PostulacionForm()
    return render(request, 'postulacion.html', {'form': form})
