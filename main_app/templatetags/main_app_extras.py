from django import template

register = template.Library()

@register.filter
def concat(a, b):
    return str(a) + str(b)
