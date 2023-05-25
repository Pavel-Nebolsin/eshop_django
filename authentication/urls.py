from django.urls import path
from .views import *

urlpatterns = [
    path('login/', LoginView.as_view(template_name='women/login.html'), name='login'),
    path('register/', RegisterView.as_view(template_name='women/register.html'), name='register'),
    path('logout/', logout_view, name="logout"),
]
