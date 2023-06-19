from django.http import HttpResponse, JsonResponse, Http404
from django.shortcuts import render, redirect
from django.views import View
from django.views.decorators.csrf import csrf_exempt
import json

from django.views.generic import DetailView

from .models import *
from .forms import MessageForm
from .utils import save_message, process_msg_data, send_reply


@csrf_exempt
def bot_webhook(request):
    # Веб хук для Телеграм бота
    if request.method == 'POST':
        msg_json = json.loads(request.body.decode('utf-8'))
        if 'message' in msg_json:  # отделяю сообщения от других апдейтов бота
            try:
                data = process_msg_data(msg_json)
            except Exception:
                raise Exception('Wrong data')

            save_message(data)

        return JsonResponse({'success': True}, status=200)
    else:
        raise Http404("Page not found")


class ChatListView(View):
    def get(self, request, chat_id):
        form = MessageForm()
        chats = TelegramUser.objects.all()
        try:
            selected_chat = TelegramUser.objects.get(chat_id=chat_id)
        except:
            selected_chat = TelegramUser.objects.all().first()

        selected_chat_messages = TelegramMessage.objects.filter(telegram_user=selected_chat)

        return render(request, 'bot_chat_list.html',
                      {'form': form,
                       'chats': chats,
                       'selected_chat_messages': selected_chat_messages,
                       'selected_chat': selected_chat})

    def post(self, request, chat_id):
        # обработка пост запроса для ответа админа в чате
        form = MessageForm(request.POST)
        if form.is_valid():
            admin_reply = form.cleaned_data['text']
            telegram_user = TelegramUser.objects.get(chat_id=chat_id)
            TelegramMessage.objects.create(
                telegram_user=telegram_user,
                message=admin_reply,
                is_admin_reply=True
            ).save()  # сохранить сообщение в ДБ
            send_reply(chat_id, admin_reply)  # отправить сообщение в телеграм чат

            return redirect('bot-chat-list', chat_id=chat_id)
        else:

            return render(request, 'bot_chat_list.html', {'form': form, 'chat_id': chat_id})
