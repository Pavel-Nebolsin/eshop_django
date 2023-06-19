from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.generic import DetailView

from shop.models import Product
from . import urls
from .models import ProductInOrder, Order, OrderStatus


def cart_view(request):
    return render(request, 'cart_view.html')


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

        return JsonResponse({'success': True, 'cart_count': cart_count})

    return JsonResponse({'success': False})


def update_quantity(request):
    if request.method == 'POST':
        item_id = int(request.POST.get('item_id'))
        quantity = int(request.POST.get('quantity'))

        try:
            cart_item = ProductInOrder.objects.get(id=item_id)
            cart_item.quantity = quantity
            cart_item.save()
            total_price = cart_item.total_price

            return JsonResponse({'success': True, 'total_price': total_price, 'item_id': item_id})
        except:
            return JsonResponse({'success': False})


    return JsonResponse({'success': False})


def delete_item(request, item_id):
    if request.method == 'POST':
        try:
            cart_item = ProductInOrder.objects.get(id=item_id)
            cart_item.delete()
        except:
            pass

        return JsonResponse({'success': True})

    return JsonResponse({'success': False})


def cart_to_pay(request, order_id):
    if request.user.is_authenticated:
        order_to_pay = Order.objects.get(id=order_id)
        order_to_pay.status_id = Order.STATUS_WAITING_FOR_PAYMENT
        order_to_pay.save()
        return redirect('user-account-orders')
    return redirect('index')


class OrderDetailView(DetailView):
    model = Order
    template_name = 'order_details.html'
    context_object_name = 'order'
