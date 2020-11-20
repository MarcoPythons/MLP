

from django.urls import path

from .Cviews import *

app_name = "carro"
urlpatterns = [
    path('add_producto/<int:producto_id>', add_producto , name = 'add_producto'),
    path('remove_producto/<int:producto_id>', remove_producto , name = 'remove_producto'),
    path('decrement_producto/<int:producto_id>', decrement_producto , name = 'decrement_producto'),
    path('clear_carro/<int:producto_id>', clear_carro , name = 'clear_carro'), 
]
