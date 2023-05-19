from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, redirect


def index(request):
    if (request.method == 'GET'):
        titulo = 'Titulo cuando accedo por get'
    else:
        titulo = f'Titulo cuando accedo por otro metodo'
    parameters_get = request.GET.get('algo')
    # return HttpResponse('Hola loco')
    return  render(request, 'index.html', {'titulo' : titulo, 'parametro' : parameters_get})

def ver_proyectos(request, anio, mes):
    return HttpResponse(f"""
        <h1>Proyectos del - {mes}/{anio}</h1>
        <p>Listado de proyectos</p>
    """)

def cursos(request, nombre):
    return HttpResponse(f'{nombre}')

def curso_detalle(request, nombre_curso):
    return HttpResponse(f'{nombre_curso}')

def redireccion(request):
    return redirect(reverse('saludar_ingles'))





# def url_invalida2(request):
#     return HttpResponse("Url invalida2 Desde la Sub App", status = 404)

# def index(request):
#     # Codigo para generar dinamismo
#     return  HttpResponse("<h1>Hola mundo!!</h1>", status = 200)

def english(request):
    # Codigo para generar dinamismo
    return  HttpResponse("<h1>Hello World!!</h1>", status = 200)

# def saludar(request, nombre):
#     return HttpResponse(f"Hola {nombre.upper()}")
# def calcular(request, numero):
#     doble = numero*2
#     return HttpResponse(f"El doble es: {doble}")