from django.contrib import admin
from registros.models import usuario



class ClienteAdmin(admin.ModelAdmin):
    list_display=("nombre" , "apellido" )
    search_fields =("nombre",)

admin.site.register(usuario, ClienteAdmin)
