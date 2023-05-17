from django.shortcuts import render
from shop.models import Product, Category
from main.cache_utils import get_categories

def product_details(request, slug):
    categories = get_categories
    item = Product.objects.get(slug=slug)
    context = {
        'item': item,
        'categories': categories,
    }
    return render(request, 'product_details.html', context)

def sort_by_category(request, category_slug):
    categories = get_categories
    selected_category = Category.objects.get(slug=category_slug)
    items = Product.objects.filter(category=selected_category)

    context = {
        'items': items,
        'categories': categories,
    }

    return render(request, 'index.html', context)
