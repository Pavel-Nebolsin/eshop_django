# Generated by Django 4.2.1 on 2023-06-17 08:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bot', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='telegrammessage',
            name='chat_id',
        ),
        migrations.RemoveField(
            model_name='telegrammessage',
            name='name',
        ),
        migrations.RemoveField(
            model_name='telegrammessage',
            name='user',
        ),
        migrations.CreateModel(
            name='TelegramUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chat_id', models.BigIntegerField(verbose_name='Chat ID')),
                ('name', models.CharField(max_length=255, verbose_name='Имя в Телеграме')),
                ('user', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Покупатель')),
            ],
        ),
        migrations.AddField(
            model_name='telegrammessage',
            name='telegram_user',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='bot.telegramuser', verbose_name='Телеграм Аккаунт'),
        ),
    ]