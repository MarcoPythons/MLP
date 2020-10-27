from django.shortcuts import render
from registros.models import cliente
# Create your views here.

def registro(request):
    return render(request, "registar.html")



def registro_completo(request):

    rut = request.POST["rut"]

    rut.save()



    return(request, "registrar.html")



