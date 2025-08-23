from django.http import HttpResponseRedirect
from django.shortcuts import render
from django import forms
from .models import *

class BeneficiarioForm(forms.ModelForm):
    class Meta:
        model = Beneficiario
        fields = ('ID', 'Nombre', 'FechaDeCreacion', 'RegionDeCreacion', 'Direccion', 'TipoDePersona', 'TipoDeEmpresa', 'Perfil', 'RUTdeEmpresa', 'RUTdeRepresentante')

def VerFormularioBeneficiario(request):
    context = {}
    if request.method == 'POST':
        form = BeneficiarioForm(request.POST)
        if form.is_valid():
            obj = Beneficiario(**form.cleaned_data)
            obj.save()
    if request.method == 'GET':
        form = BeneficiarioForm()
        context['nombre'] = 'Nombre'
        context['fechadecreacion'] = 'FechaDeCreacion'
        context['regiondecreacion'] = 'RegionDeCreacion'
        context['direccion'] = 'Direccion'
        context['tipodepersona'] = 'TipoDePersona'
        context['tipodeempresa'] = 'TipoDeEmpresa'
        context['perfil'] = 'Perfil'
        context['rutdeempresa'] = 'RUTdeEmpresa'
        context['rutderepresentante'] = 'RUTdeRepresentante'
    return render(request, 'form.html', {'form': form})

class ProyectoForm(forms.ModelForm):
    class Meta:
        model = Proyecto
        fields = ('ID', 'Beneficiario', 'Titulo', 'Descripcion', 'DuracionEnMesesMinimo', 'DuracionEnMesesMaximo', 'Alcance', 'Area')

def VerFormularioProyecto(request):
    context = {}
    if request.method == 'POST':
        form = ProyectoForm(request.POST)
        if form.is_valid():
            obj = Proyecto(**form.cleaned_data)
            obj.save()
    if request.method == 'GET':
        form = ProyectoForm()
        context['beneficiario'] = 'Beneficiario'
        context['titulo'] = 'Titulo'
        context['descripcion'] = 'Descripcion'
        context['duracionenmesesminimo'] = 'DuracionEnMesesMinimo'
        context['duracionenmesesmaximo'] = 'DuracionEnMesesMaximo'
        context['alcance'] = 'Alcance'
        context['area'] = 'Area'
    return render(request, 'form.html', {'form': form})

class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = ('ID', 'Nombre', 'Sexo', 'RUT')

def VerFormularioPersona(request):
    context = {}
    if request.method == 'POST':
        form = PersonaForm(request.POST)
        if form.is_valid():
            obj = Persona(**form.cleaned_data)
            obj.save()
    if request.method == 'GET':
        form = PersonaForm()
        context['nombre'] = 'Nombre'
        context['sexo'] = 'Sexo'
        context['rut'] = 'RUT'
    return render(request, 'form.html', {'form': form})

class MiembroForm(forms.ModelForm):
    class Meta:
        model = Miembro
        fields = ('ID', 'Persona', 'Beneficiario')

def VerFormularioMiembro(request):
    context = {}
    if request.method == 'POST':
        form = MiembroForm(request.POST)
        if form.is_valid():
            obj = Miembro(**form.cleaned_data)
            obj.save()
    if request.method == 'GET':
        form = MiembroForm()
        context['persona'] = 'Persona'
        context['beneficiario'] = 'Beneficiario'
    return render(request, 'form.html', {'form': form})

class ColaboradorForm(forms.ModelForm):
    class Meta:
        model = Colaborador
        fields = ('ID', 'Persona', 'Proyecto')

def VerFormularioColaborador(request):
    context = {}
    if request.method == 'POST':
        form = ColaboradorForm(request.POST)
        if form.is_valid():
            obj = Colaborador(**form.cleaned_data)
            obj.save()
    if request.method == 'GET':
        form = ColaboradorForm()
        context['persona'] = 'Persona'
        context['proyecto'] = 'Proyecto'
    return render(request, 'form.html', {'form': form})

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ('ID', 'Persona', 'NombreDeUsuario', 'Contrasena', 'Correo')

def VerFormularioUsuario(request):
    context = {}
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            obj = Usuario(**form.cleaned_data)
            obj.save()
    if request.method == 'GET':
        form = UsuarioForm()
        context['persona'] = 'Persona'
        context['nombredeusuario'] = 'NombreDeUsuario'
        context['contrasena'] = 'Contrasena'
        context['correo'] = 'Correo'
    return render(request, 'form.html', {'form': form})

class ConsorcioForm(forms.ModelForm):
    class Meta:
        model = Consorcio
        fields = ('ID', 'PrimerBeneficiario', 'SegundoBeneficiario')

def VerFormularioConsorcio(request):
    context = {}
    if request.method == 'POST':
        form = ConsorcioForm(request.POST)
        if form.is_valid():
            obj = Consorcio(**form.cleaned_data)
            obj.save()
    if request.method == 'GET':
        form = ConsorcioForm()
        context['primerbeneficiario'] = 'PrimerBeneficiario'
        context['segundobeneficiario'] = 'SegundoBeneficiario'
    return render(request, 'form.html', {'form': form})

class FinanciadorForm(forms.ModelForm):
    class Meta:
        model = Financiador
        fields = ('ID', 'Nombre', 'FechaDeCreacion', 'RegionDeCreacion', 'Direccion', 'TipoDePersona', 'TipoDeEmpresa', 'Perfil', 'RUTdeEmpresa', 'RUTdeRepresentante')

def VerFormularioFinanciador(request):
    context = {}
    if request.method == 'POST':
        form = FinanciadorForm(request.POST)
        if form.is_valid():
            obj = Financiador(**form.cleaned_data)
            obj.save()
    if request.method == 'GET':
        form = FinanciadorForm()
        context['nombre'] = 'Nombre'
        context['fechadecreacion'] = 'FechaDeCreacion'
        context['regiondecreacion'] = 'RegionDeCreacion'
        context['direccion'] = 'Direccion'
        context['tipodepersona'] = 'TipoDePersona'
        context['tipodeempresa'] = 'TipoDeEmpresa'
        context['perfil'] = 'Perfil'
        context['rutdeempresa'] = 'RUTdeEmpresa'
        context['rutderepresentante'] = 'RUTdeRepresentante'
    return render(request, 'form.html', {'form': form})

class InstrumentoForm(forms.ModelForm):
    class Meta:
        model = Instrumento
        fields = ('ID', 'Titulo', 'Financiador', 'Alcance', 'Descripcion', 'FechaDeApertura', 'FechaDeCierre', 'DuracionEnMeses', 'Beneficios', 'Requisitos', 'MontoMinimo', 'MontoMaximo', 'Estado', 'TipoDeBeneficio', 'TipoDePerfil', 'EnlaceDelDetalle', 'EnlaceDeLaFoto')

def VerFormularioInstrumento(request):
    context = {}
    if request.method == 'POST':
        form = InstrumentoForm(request.POST)
        if form.is_valid():
            obj = Instrumento(**form.cleaned_data)
            obj.save()
    if request.method == 'GET':
        form = InstrumentoForm()
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
    return render(request, 'form.html', {'form': form})

class PostulacionForm(forms.ModelForm):
    class Meta:
        model = Postulacion
        fields = ('ID', 'Beneficiario', 'Proyecto', 'Instrumento', 'Resultado', 'MontoObtenido', 'FechaDePostulacion', 'FechaDeResultado', 'Detalle')

def VerFormularioPostulacion(request):
    context = {}
    if request.method == 'POST':
        form = PostulacionForm(request.POST)
        if form.is_valid():
            obj = Postulacion(**form.cleaned_data)
            obj.save()
    if request.method == 'GET':
        form = PostulacionForm()
        context['beneficiario'] = 'Beneficiario'
        context['proyecto'] = 'Proyecto'
        context['instrumento'] = 'Instrumento'
        context['resultado'] = 'Resultado'
        context['montoobtenido'] = 'MontoObtenido'
        context['fechadepostulacion'] = 'FechaDePostulacion'
        context['fechaderesultado'] = 'FechaDeResultado'
        context['detalle'] = 'Detalle'
    return render(request, 'form.html', {'form': form})
