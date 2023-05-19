from .models import Order, OrderStatus
from django.core.cache import cache


def cart(request):
    status = cache.get('status')
    if not status:
        status = OrderStatus.objects.get(name='Корзина')
        cache.set('status', status)

    if request.user.is_authenticated:
        user = request.user
        cart, _ = Order.objects.get_or_create(user=user, status=status)

    else:
        session_key = request.session.session_key
        if not session_key:
            request.session.cycle_key()
            session_key = request.session.session_key

        cart, _ = Order.objects.get_or_create(session_key=session_key, status=status)

    cart_count = cart.productinorder_set.count()
    cart_total_amount = cart.total_amount

    return {'cart': cart, 'cart_count': cart_count,'cart_total_amount': cart_total_amount}
