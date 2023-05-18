from django.http import JsonResponse
from django.shortcuts import render
from shop.models import Product
from .models import ProductInOrder, Order


def order_details(request, pk):
    return render(request, 'order_details.html', context={'pk': pk})


def add_to_cart(request):
    if request.method == 'POST':

        slug = request.POST.get('slug')
        quantity = int(request.POST.get('quantity'))
        order_id = int(request.POST.get('order_id'))

        product = Product.objects.get(slug=slug)
        cart = Order.objects.get(id=order_id)

        cart_item, created = ProductInOrder.objects.get_or_create(
            product=product,
            order=cart
        )
        if created:
            cart_item.quantity = quantity
        else:
            cart_item.quantity += quantity
        cart_item.save()
        cart_count = cart.productinorder_set.count()
        return JsonResponse({'success': True,'cart_count': cart_count })

    return JsonResponse({'success': False})

