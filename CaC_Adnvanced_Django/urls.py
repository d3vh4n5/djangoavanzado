"""CaC_Adnvanced_Django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from . import views #Primero importa las vistas del proyecto

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', views.url_invalida),#Si está vacio en la url sin path
    #path('hola_mundo/', include('miproyecto.urls')),
    path('', include('miproyecto.urls')),#Con esto hacemos que por defecto, al no escribir una ruta, nos redirija a nuestra subaplicacion de mirpoyecto como analizador de rutas principal
]

