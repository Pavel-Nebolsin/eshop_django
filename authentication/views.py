from allauth.account.adapter import get_adapter
from allauth.account import app_settings
from allauth.account.utils import complete_signup
from allauth.exceptions import ImmediateHttpResponse
from django.contrib.auth import logout, authenticate, login
from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import render, redirect
from order.models import Order
from allauth.account.views import LoginView, SignupView
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter


def register_view(request):
    pass


def logout_view(request):
    logout(request)
    return redirect('index')


def set_cart_to_user(cart_id, user):
    cart = Order.objects.get(id=cart_id)
    if cart.productinorder_set.count() > 0:

        old_user_cart = Order.objects.filter(user=user, status_id=Order.STATUS_CART).first()
        if old_user_cart:
            old_user_cart.delete()

        cart.user = user
        cart.session_key = None
        cart.save()

    else:
        cart.delete()


class CustomLoginView(LoginView):
    # переопределение метода allauth для перерегистрации текущей корзины
    # на авторизованного пользователя
    def form_valid(self, form):
        success_url = self.get_success_url()
        try:
            cart_id = self.request.session.get('cart_id')
            user = form.user
            set_cart_to_user(cart_id, user)
            print("---------- Custom LOGIN View -----------")
            return form.login(self.request, redirect_url=success_url)
        except ImmediateHttpResponse as e:
            return e.response


class CustomSignUpView(SignupView):
    # переопределение метода allauth для перерегистрации текущей корзины
    # на нового зарегистрированного пользователя
    def form_valid(self, form):
        self.user = form.save(self.request)
        if not self.user:
            return get_adapter(self.request).respond_email_verification_sent(
                self.request, None
            )
        try:
            cart_id = self.request.session.get('cart_id')
            user = self.user
            set_cart_to_user(cart_id, user)
            print("---------- Custom SIGNUP View -----------")
            return complete_signup(
                self.request,
                self.user,
                app_settings.EMAIL_VERIFICATION,
                self.get_success_url(),
            )
        except ImmediateHttpResponse as e:
            return e.response

    def form_invalid(self, form):
        errors = {field.name: field.errors for field in form}
        return JsonResponse({'success': False, 'errors': errors}, status=400)

#
class CustomSocialAccountAdapter(DefaultSocialAccountAdapter):
    # переопределение метода allauth(social accounts) для перерегистрации
    # текущей корзины на нового, подключенного соц аккаунта пользователя
    def save_user(self, request, sociallogin, form=None):
        # Вызываем базовую реализацию для создания пользователя
        user = super().save_user(request, sociallogin, form)
        # регистрируем корзину на нового пользователя
        cart_id = self.request.session.get('cart_id')
        print("save_user", cart_id, user)
        set_cart_to_user(cart_id, user)
        messages.success(request, 'Successful login')  # Добавляем в сессию сообщение об успешном входе
        return user

    # переопределение метода allauth(social accounts) для перерегистрации
    # текущей корзины на уже существующего в нашей БД пользователя
    def pre_social_login(self, request, sociallogin):
        if sociallogin.is_existing:
            user = sociallogin.user
            cart_id = self.request.session.get('cart_id')
            print("pre_social_login", cart_id, user)
            # регистрируем корзину на нового пользователя
            set_cart_to_user(cart_id, user)
            messages.success(request, 'Successful login')  # Добавляем в сессию сообщение об успешном входе
