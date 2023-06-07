from django.urls import path
from .views import *

urlpatterns = [
    path('register/', register_view, name='register'),
    path('logout/', logout_view, name="logout"),
    path('email-confirm/<int:user_id>', email_confirm_view, name="email-confirm"),
]
