from django.contrib import admin

from .models import TelegramMessage, TelegramUser


@admin.register(TelegramMessage)
class TelegramMessageAdmin(admin.ModelAdmin):
    list_display = [field.name for field in TelegramMessage._meta.get_fields()]

@admin.register(TelegramUser)
class TelegramUserAdmin(admin.ModelAdmin):
    list_display = [field.name for field in TelegramUser._meta.get_fields()]
