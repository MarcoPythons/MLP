from django.db import models
import registros.models as registros

# Create your models here.


class carrito (models.Model): 
    fecha_creacion = models.DateField(null = False)


    class Meta:
        db_table = 'carrito'
        ordering = ['fecha_creacion']



class producto(models.Model):
    precio = models.IntegerField(null = False)
    tipo = models.CharField(max_length = 30, null = False)
    
    class Meta:
        db_table = 'producto'
        ordering = ['id']

    
class pedido(models.Model):
     fecha_realizacion = models.DateField(null = False)
     estado = models.CharField(max_length = 10, null = False)
     total = models.IntegerField(null = False)
     
     class Meta:
         db_table = 'pedido'
         ordering = ['fecha_realizacion']


class pago(models.Model):
    fecha_pago = models.DateField(null = False)
    monto_pago = models.IntegerField(null = False)
    metodo_pago = models.CharField(max_length = 10, null = False)

    class Meta:
        db_table = 'pago'
        ordering = ['fecha_pago']





