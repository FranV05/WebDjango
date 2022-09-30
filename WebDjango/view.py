from django.http import HttpResponse
from django.template import loader

def home(request, name):
    return HttpResponse(f"Hola soy {name}")

def inicio(request):
    return HttpResponse(f"Hola soy inicio WebDjango")

def homePage(self):
    lista = [1,2,3,4,5,6,7,8,9]
    data = {'nombre':'Francisco', 'apellido': 'Vega', 'lista': lista}
    planilla = loader.get_template('home.html')
    documento = planilla.render(data)
    return HttpResponse(documento)