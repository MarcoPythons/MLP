"""MLP URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from registros import Rviews
from MLP import views
from carro import Cviews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('registro/', Rviews.registro, name='registro'),
    path('User-Created/', Rviews.registro_completo, name='registrado'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('home/',views.pag_principal, name ='pag_principal'), 
    path('tienda/muebleria-los-pinos', Cviews.tienda , name = 'tienda'),
    path('carro/muebleria-los-pinos', Cviews.carro , name = 'carro'),
    path('checkout/', Cviews.checkout , name = 'checkout')
]
