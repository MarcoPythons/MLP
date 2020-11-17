from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import login, authenticate




def tienda(request):

    return render(request, "tienda.html")


def carro(request):

    return render(request, "carro.html")


def checkout(request):

    return render(request, "checkout.html")