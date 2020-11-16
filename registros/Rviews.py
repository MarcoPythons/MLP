from django.shortcuts import render, redirect, HttpResponse
from registros.models import usuario
from registros.forms import ClienteForm
from django.contrib.auth import login, authenticate


def registro(request):

    data = {
        'form': ClienteForm
    }

    if request.method == 'POST':
        formulario = ClienteForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            username = formulario.cleaned_data['username']
            password = formulario.cleaned_data['password2']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect(to='/home/')

    return render(request, "registar.html", data)


def registro_completo(request):

    rut_desde_html = request.POST["rut"]

    # run_desde_bd=cliente.objects.filter(run__exact = rut_desde_html)

    return render(request, "registro_completo.html")
