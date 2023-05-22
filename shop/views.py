from django.shortcuts import render
from shop.models import Product, Category


def product_details(request, slug):
    item = Product.objects.get(slug=slug)
    context = {
        'item': item,
    }
    return render(request, 'product_details.html', context)

def sort_by_category(request, category_slug):
    items = Category.objects.get(slug=category_slug).product_set.all()
    context = {
        'items': items,
    }
    return render(request, 'index.html', context)
