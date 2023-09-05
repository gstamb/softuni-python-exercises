from django import template
register = template.Library()

@register.filter()
def capitalize_func(value):
    return value.capitalize()