from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('account/', user_account_view, name='user-account'),

]