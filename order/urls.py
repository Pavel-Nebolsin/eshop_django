from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('cart/', cart_view, name='cart-view'),
    path('add-to-cart/', add_to_cart, name='add-to-cart'),
    path('update-quantity/', update_quantity, name='update-quantity'),
    path('delete-item/<int:item_id>', delete_item, name='delete-item'),
    path('cart/cart-to-pay/<int:order_id>', cart_to_pay, name='cart-to-pay'),
    path('order-details/<int:pk>', OrderDetailView.as_view(), name='order-details'),

]
