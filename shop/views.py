from django.shortcuts import render


def product_details(request, pk):
    pk = pk
    return render(request, 'product_details.html')
