from django.contrib import admin
from registros.models import usuario



class ClienteAdmin(admin.ModelAdmin):
    list_display=("nombre" , "apellido" , "run")
    search_fields =("run",)

admin.site.register(usuario, ClienteAdmin)
