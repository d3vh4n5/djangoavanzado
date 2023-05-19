from django.shortcuts import render
from django.http import HttpResponse

def url_invalida(request):
    return HttpResponse("Url invalida Desde el proyecto principal", status = 404)