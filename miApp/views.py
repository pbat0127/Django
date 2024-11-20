from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def miApp(request):
    return HttpResponse("Ve a la página de Bienvenida para más información!")

def Bienvenida(request):
    template = loader.get_template('miPrimerTemplate.html')
    return HttpResponse(template.render())

