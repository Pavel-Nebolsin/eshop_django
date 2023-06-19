from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('account/', user_account_view, name='user-account'),
    path('account/orders', UserOrdersListView.as_view(), name='user-account-orders'),
    path('account/contact', user_contact_view, name='user-account-contact'),
]