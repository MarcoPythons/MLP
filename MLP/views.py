from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import login, authenticate
from carro.models import producto



def pag_principal(request):

    productos = producto.objects.all()

    data = {
        'productos':productos
    }

    return render(request, 'index.html',data)
