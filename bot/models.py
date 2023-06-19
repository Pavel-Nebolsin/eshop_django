from django.contrib.auth.models import User
from django.db import models


class TelegramMessage(models.Model):
    telegram_user = models.ForeignKey('TelegramUser', on_delete=models.CASCADE, blank=True, null=True, default=None,
                                      verbose_name='Телеграм Аккаунт')
    message = models.TextField(verbose_name='Сообщение')
    is_admin_reply = models.BooleanField(default=False,verbose_name='Ответ Админа')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Создан')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Обновлён')

    def __str__(self):
        return self.message


class TelegramUser(models.Model):
    chat_id = models.BigIntegerField(verbose_name='Chat ID')
    name = models.CharField(max_length=255, verbose_name='Имя в Телеграме')

    def __str__(self):
        return f'{self.name} - {self.chat_id}'
