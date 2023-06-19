from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from .models import TelegramMessage, TelegramUser
import requests


def save_message(data):

    telegram_user, _ = TelegramUser.objects.get_or_create(
        chat_id=data['chat_id'], defaults={'name': data['first_name']})

    message = TelegramMessage.objects.create(
        telegram_user=telegram_user, message=data['text'])

    message.save()


def send_reply(chat_id,text):
    reply_url = f"https://api.telegram.org/bot5774654090:AAFq4w59KOhKlDeQ353g6zZUiPafK3dyrPI/sendMessage"

    data = {"chat_id": chat_id, "text": text}
    requests.post(reply_url, data=data)


def process_msg_data(update):
    print(update)
    message = update['message']
    if "first_name" in message["from"]:
        first_name = message["from"]["first_name"]
    else:
        first_name = "Anonymus"
    if "last_name" in message["from"]:
        last_name = message["from"]["last_name"]
    else:
        last_name = "Anonymus"

    if "text" in message:
        text = message['text']
    else:
        text = '[ gif ]'

    chat_id = message['chat']['id']
    return {
        'first_name': first_name,
        'last_name': last_name,
        'text': text,
        'chat_id': chat_id,
    }

