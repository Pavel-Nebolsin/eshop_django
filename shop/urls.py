from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('details/<int:pk>', product_details, name='product_details'),
]
