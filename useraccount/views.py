from django.shortcuts import render
from order.models import Order


def user_account_view(request):
    user = request.user
    orders = Order.objects.all().filter(user=user, status_id=Order.STATUS_WAITING_FOR_PAYMENT)
    context = {
        'orders': orders
    }
    return render(request, 'user_account_main.html', context)
