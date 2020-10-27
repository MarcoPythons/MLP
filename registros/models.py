from django.db import models

# Create your models here.

class cliente(models.Model):
    id = models.AutoField(primary_key=True)
    run = models.CharField(max_length=10, null=False)
    direccion = models.CharField(max_length=60, null=False)
    telefono = models.IntegerField(null=False)
    email = models.EmailField(null=False)

    class Meta:
        db_table = 'cliente'
        ordering = ['run']

class cuenta(models.Model):
    run = models.OneToOneField(cliente , max_length=10, primary_key=True, on_delete = models.CASCADE)
    password = models.CharField(max_length=15, null=False) 

    class Meta:
        db_table = 'cuenta'
        ordering = ['run']
