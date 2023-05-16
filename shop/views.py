from django.shortcuts import render
from shop.models import Product

def product_details(request, slug):
    item = Product.objects.get(slug=slug)
    context = {
        'item': item,
    }
    return render(request, 'product_details.html', context)
