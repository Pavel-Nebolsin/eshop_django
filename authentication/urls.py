from django.urls import path, include
from .views import *

urlpatterns = [
    path('register/', register_view, name='register'),
    path('logout/', logout_view, name="logout"),
    # allauth urls
    path('accounts/', include('allauth.urls')),
    path('login/', CustomLoginView.as_view(), name='account_login'),
    path('signup/', CustomSignUpView.as_view(), name='account_signup'),
    path('change-password/', CustomPasswordChangeView.as_view(), name='account_change_password'),
    path('set-password/', CustomPasswordSetView.as_view(), name='account_set_password'),
    path('send-email-confirm/<int:user_id>', email_confirm_view, name="email-confirm"),
    path('confirm-email/<str:key>/', CustomConfirmEmailView.as_view(), name='account_confirm_email'),
]
