from django import template
from templates_advanced.todos.models import Todo
register = template.Library()

@register.simple_tag
def todos_count():
    objs = Todo.objects.count()
    return   objs


@register.inclusion_tag('shared/templatetags/todos_preview.html', takes_context=True,)
def todos_preview(context):
    return {
        'count': Todo.objects.count()
    }
    
@register.filter
def get_type(value):
    return type(value)