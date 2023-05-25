from django.shortcuts import render
from shop.models import Product


def index(request):
    items = Product.objects.all()
    context = {
        'items': items,
    }
    return render(request, 'index.html', context)
