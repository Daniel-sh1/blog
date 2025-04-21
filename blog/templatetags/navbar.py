# Файл some_tags.py 
from django import template
from blog.models import Categories

register = template.Library()

@register.simple_tag()
def get_categoryes():
    return Categories.objects.all()