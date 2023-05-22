from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('cart/', cart_view, name='cart-view'),
    path('add-to-cart/', add_to_cart, name='add-to-cart'),
    path('cart/update-quantity/', update_quantity, name='update-quantity'),
    path('cart/delete-item/<int:item_id>', delete_cart_item, name='delete-cart-item'),
    path('cart/order-to-pay/<int:order_id>', order_to_pay, name='order-to-pay'),
]
