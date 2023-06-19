from django.shortcuts import render
from django.views.generic import DetailView, ListView

from shop.models import Product, Category

class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_details.html'
    context_object_name = 'item'


class ProductsListView(ListView):
    model = Product
    template_name = 'index.html'
    context_object_name = 'items'

    def get_queryset(self):
        queryset = super().get_queryset()
        slug = self.kwargs.get('slug')
        return queryset.filter(category__slug=slug)
