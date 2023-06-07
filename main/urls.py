from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from . import settings
from .views import *
from authentication.views import CustomLoginView, CustomSignUpView, CustomConfirmEmailView

urlpatterns = [
    path('', index, name='index'),
    path('admin/', admin.site.urls),
    path('shop/', include('shop.urls')),
    path('order/', include('order.urls')),
    path('user/', include('useraccount.urls')),
    path('auth/', include('authentication.urls')),
    # allauth urls
    path('accounts/login/', CustomLoginView.as_view(), name='account_login'),
    path('accounts/signup/', CustomSignUpView.as_view(), name='account_signup'),
    path('accounts/confirm-email/<str:key>/', CustomConfirmEmailView.as_view(), name='account_confirm_email'),
    path('accounts/', include('allauth.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
