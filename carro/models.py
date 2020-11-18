from registros.forms import ClienteForm
from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField
from registros.models import usuario as Cliente

# Create your models here.



class producto(models.Model):
    precio = models.IntegerField(null=False)
    tipo = models.CharField(max_length=30, null=False)
    descripcion = models.CharField(max_length=400)
    image= models.ImageField(null=False)

    class Meta:
        db_table = 'producto'
        ordering = ['id']


class datos_envio_cliente(models.Model):
    adress=models.CharField(null=False,max_length=70)
    adress2=models.CharField(null=True,max_length=70)
    country=models.CharField(null=False,max_length=70)
    state=models.CharField(null=False,max_length=70)
    zip_code=models.CharField(null=False,max_length=70)
    metodo_envio=CharField(null=False,max_length=70)
    cliente_id = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    class Meta:
        db_table = 'Datos_envio_cliente'


class pedido(models.Model):
    subtotal = models.IntegerField(null=False)
    descuento = models.IntegerField(null=False)
    cupon = models.IntegerField(null=False)
    costo_envio = models.IntegerField(null=False)
    total_compra = models.IntegerField(null=False)
    metodo_pago = models.CharField(null=False,max_length=70)

    class Meta:
        db_table = 'pedido'
