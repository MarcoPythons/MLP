from django.http import request
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import login, authenticate
from carro.models import producto
from carro.carro import Carro
from registros.models import usuario








def add_producto(request,producto_id):
    carro = Carro(request)
    productos = producto.objects.get(id=producto_id)
    carro.add(producto=productos)
    return redirect("tienda")

def remove_producto(request,producto_id):
    carro=Carro(request)
    productos=producto.objects.get(id=producto_id)
    carro.remove(productos)
    return redirect("carrito1")

def decrement_producto(request, producto_id):
    carro1=Carro(request)
    productos=producto.objects.get(id=producto_id)
    carro1.decrement(productos)
    return redirect("carrito1")


def clear_carro(request,producto_id):
    carro = Carro(request)
    carro.clear()
    return redirect("carrito1")




def tienda(request):

    productos = producto.objects.all()
    data = {
        'productos':productos
    } 

    return render(request, "tienda.html",data)


def carrito1(request):
    carro=Carro(request)

    return render(request, "carro.html")


def checkout(request):


    return render(request, "checkout.html")