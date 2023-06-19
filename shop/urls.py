from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('details/<str:slug>', ProductDetailView.as_view(), name='product_details'),
    path('category/<str:slug>', ProductsListView.as_view(), name='category'),
]
