from .models import Order, OrderStatus
from django.core.cache import cache


def cart(request):

    if request.user.is_authenticated:
        user = request.user
        cart, _ = Order.objects.get_or_create(user=user, status_id=Order.STATUS_CART)

    else:
        session_key = request.session.session_key
        if not session_key:
            request.session.cycle_key()
            session_key = request.session.session_key

        cart, _ = Order.objects.get_or_create(session_key=session_key, status_id=Order.STATUS_CART)

    cart_count = cart.productinorder_set.count()
    cart_total_amount = cart.total_amount
    cart_id = cart.id
    request.session['cart_id'] = cart_id

    return {
        'cart': cart,
        'cart_id': cart_id,
        'cart_count': cart_count,
        'cart_total_amount': cart_total_amount
    }
