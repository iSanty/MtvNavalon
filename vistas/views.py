
from django.http import HttpResponse
from datetime import datetime
#from primerasvistas.models import Familiar

from django.template import Template, Context, loader


def inicio(request):
    return HttpResponse('hola soy mi primer vista')



def mi_template(request):
    
    template1 = loader.get_template('inicio.html')

    nombre = 'Santiago Navalon'
    nombre2 = "Rodrigo Gimenez"
    #familiar = Familiar(nombre_familiar='Marcelo', edad=50)
    #familiar.save()
    render1 = template1.render(
        {'nombre': nombre, 'nombre2': nombre2})
    
    return HttpResponse(render1)


    
def saludo(request, nombre):
    return HttpResponse(f'Hola : {nombre} ')
    
    
def ver_fecha(request):
    fecha_actual = datetime.now()
    return HttpResponse(f'fecha actual: {fecha_actual} ')