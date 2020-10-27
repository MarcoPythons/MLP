from django.shortcuts import render
from registros.models import cliente
# Create your views here.


def registro(request):

    return render(request, "registar.html")

def registro_completo(request):


    rut_desde_html =request.POST["rut"]

    run_desde_bd=cliente.objects.filter(run__exact = rut_desde_html)
    

    return render(request, "registro_completo.html")
