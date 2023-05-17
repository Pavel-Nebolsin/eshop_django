from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('details/<str:slug>', product_details, name='product_details'),
    path('category/<str:category_slug>', sort_by_category, name='category'),
]
