from django import template

register = template.Library()

@register.filter
def get_attribute(obj, attr_name):
    return getattr(obj, attr_name, '')

@register.filter
def format_title(attr_name):
    return " ".join(attr_name.split('_')).title()