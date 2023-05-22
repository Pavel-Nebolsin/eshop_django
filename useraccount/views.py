from django.shortcuts import render
from order.models import Order, OrderStatus


def user_account_view(request):
    user = request.user
    status = OrderStatus.objects.get(name='Ожидает оплаты')
    orders = Order.objects.all().filter(user=user, status=status)
    context = {
        'orders': orders
    }

    return render(request, 'user_account_main.html', context)
