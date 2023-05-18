from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('details/<int:pk>', order_details, name='order_details'),
    path('add-to-cart/', add_to_cart, name='add_to_cart'),
]
