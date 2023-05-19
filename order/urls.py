from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('cart/', cart_view, name='cart_view'),
    path('add-to-cart/', add_to_cart, name='add_to_cart'),
    path('cart/update-quantity/', update_quantity, name='update-quantity'),
]
