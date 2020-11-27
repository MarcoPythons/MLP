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
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('registro/', Rviews.registro, name='registro'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('home/',views.pag_principal, name ='pag_principal'), 
    path('tienda/muebleria-los-pinos', Cviews.tienda , name = 'tienda'),
    path('carrito1/muebleria-los-pinos', Cviews.carrito1 , name = 'carrito1'),
    path('checkout/', Cviews.checkout , name = 'checkout'),
    path('carro/', include('carro.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/',include('allauth.urls')),
    path('', include('pwa.urls')),

]
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
