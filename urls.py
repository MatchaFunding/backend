"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    '''
    path('vertodoslosBeneficiarios/', views.VerTodosLosBeneficiarios),
    path('enviarnuevoBeneficiario/', views.EnviarNuevoBeneficiario),
    path('buscarBeneficiarioporid/', views.BuscarBeneficiarioPorID),
    path('vertodoslosproyectos/', views.VerTodosLosProyectos),
    path('buscarproyectosporpost', views.BuscarProyectosPorPost),
    path('enviarnuevoproyecto/', views.EnviarNuevoProyecto),
    path('vertodoslosproyectosporidpost/', views.VerTodosLosProyectosPorIDPost),
    path('vertodoslosmiembros/', views.VerTodosLosMiembros),
    path('vertodoslosfinanciadores/', views.VerTodosLosFinanciadores), 
    path('enviarnuevofinanciador/', views.EnviarNuevoFinanciador),  
    path('vertodoslosfondos/', views.VerTodosLosFondos),
    path('enviarnuevofondo/', views.EnviarNuevoFondo),
    path('vertodaslaspostulaciones/', views.VerTodasLasPostulaciones),
    path('enviarnuevapostulacion/', views.EnviarNuevaPostulacion),
    path('vertodoslosresultados/', views.VerTodosLosResultados),
    path('vertodaslaspaginasdefondos/', views.VerTodasLasPaginasDeFondos),
    path('vertodoslosusuariopost/', views.VerTodosLosUsuarioPost),
    path('validarcredencialesdeusuariopost/', views.ValidarCredencialesDeUsuarioPost),
    path('registrarnuevousuariopost/', views.RegistrarNuevoUsuarioPost),
    path('enviarnuevoresultado/', views.EnviarNuevoResultado),
    path('actualizarBeneficiario/', views.ActualizarBeneficiario),
    '''
]