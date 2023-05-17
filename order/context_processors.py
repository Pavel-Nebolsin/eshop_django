from .models import Order, OrderStatus


def cart(request):
    status = OrderStatus.objects.get(name='Корзина')

    if request.user.is_authenticated:  # Проверяем, залогинен ли пользователь
        user = request.user
        cart, created = Order.objects.get_or_create(user=user, status=status)

    else:
        session_key = request.session.session_key
        if not session_key:
            request.session.cycle_key()
            session_key = request.session.session_key

        cart, created = Order.objects.get_or_create(session_key=session_key, status=status)

    print(cart)
    return {'cart': cart}
