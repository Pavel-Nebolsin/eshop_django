from django import template
from django.core.cache import cache
from shop.models import Category

register = template.Library()


@register.simple_tag
def get_categories():
    categories = cache.get('categories')
    if not categories:
        categories = Category.objects.all()
        cache.set('categories', categories)
    return categories
