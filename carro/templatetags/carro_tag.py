from django import template


register = template.Library()


@register.filter()
def multiplicar(value, arg):
    return int(value)*arg

@register.filter()
def formato_moneda(value, arg):
    return f"{value}{arg}"

@register.filter()
def sumar_compra(value,value2):
    return int(value)+value2