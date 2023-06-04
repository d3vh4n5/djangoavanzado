from datetime import datetime
from django.shortcuts import render
from django.conf import settings
from .forms import ContactoForm # Esto se importó en esta clase (16)
from django.contrib import messages # Esto se importo en la clase 17


def index(request):
    saludos = ['Hola', 'Hello', 'Olá', "Buenas"]
    idioma_saludo = {'en': 'Hello', 'es': 'Hola', 'br': 'Olá'}
    return render(request, "hola_mundo/index.html", {"hoy": datetime.now, "saludos": saludos, "idioma_saludos": idioma_saludo})


def lenguajes(request):
    idiomas = ['English', 'Español', 'Portugues', 'Alemán']
    return render(request, "hola_mundo/lenguajes.html", {"lenguajes": idiomas})

def contacto(request):
    if request.method == "POST":
        # Creola instancia pupulada con los datos cargados en pantalla
        contacto_form = ContactoForm(request.POST)
        print('Algo')
        #valido y proceso los datos.
        if contacto_form.is_valid():
            messages.set_level(request, messages.DEBUG)
            messages.success(request, "Formulario cargado con éxito")
            messages.debug(request, "DEBUGG")
            messages.info(request, "Info importante")
            messages.warning(request, "Algo anda mal")
            messages.error(request, "NO ANDA")
    else:
        # Creo el formulario vacío con los valores por defecto
        contacto_form = ContactoForm()
    return render(request, "hola_mundo/contacto.html", { 'contacto_form' : contacto_form })