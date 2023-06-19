from django.urls import path, include
from .views import *

urlpatterns = [
    path('', bot_webhook, name='bot-webhook'),
    path('chat-list/<int:chat_id>', ChatListView.as_view(), name='bot-chat-list')
]
