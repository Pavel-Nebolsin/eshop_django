# Generated by Django 4.2.1 on 2023-06-17 10:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0002_remove_telegrammessage_chat_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='telegramuser',
            name='user',
        ),
    ]