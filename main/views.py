from django.shortcuts import render
from .cache_utils import get_categories
from shop.models import Product, ProductImage


def index(request):
    categories = get_categories
    items = Product.objects.all()
    context = {
        'items': items,
        'categories': categories,
    }
    return render(request, 'index.html', context)
