from django.core.checks import messages
from backend.settings import WEBHOOK_URL
from datetime import date
import requests
import json

from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.views import View


from django.conf import settings
from .models import Events, Users


class TelegramBotView(View):
    def post(self, request, *args, **kwargs):
        # JSON из полученного обновления:
        t_body = request.body
        t_data = json.loads(t_body.decode("utf-8"))
        # Добавление пользователя в базу
        usersAppend(t_data)
        # Получения id и текста из обновления
        u = getUpdate(t_data)
        text = u["text"]
        id = u["id"]

        # Все записи
        if text == "/all":
            all = Events.objects.all()
            for e in all:
                message = formatMessage(e)
                self.send_message(message, id)

        # События сегодня
        if text == "/today":
            today = date.today()
            today_filter = Events.objects.filter(
                date__month=today.month, date__day=today.day
            )
            for e in today_filter:
                message = formatMessage(e)
                self.send_message(message, id)

        return JsonResponse({"ok": "POST request processed"})

    # Отправка сообщения
    @staticmethod
    def send_message(message, chat_id):
        data = {
            "chat_id": chat_id,
            "text": message,
            "parse_mode": "Markdown",
        }
        response = requests.post(
            f"{settings.TELEGRAM_URL}{settings.TOKEN}/sendMessage", data=data
        )


# Подготовка сообщения для отправки
def formatMessage(e: Events) -> str:
    s = "*" + str(e.date) + "*" + "\n"
    s += str(e.title) + "\n"
    s += str(e.body) + "\n"
    return s


# Добавление уникального пользователя в базу
def usersAppend(r: dict):
    update = getUser(r)
    if update["id"]:
        try:
            Users.objects.get(chatId=update["id"])
        except:
            append = Users()

            append.chatId = update["id"]
            append.username = update["username"]
            append.firstName = update["first_name"]
            append.lastName = update["last_name"]

            append.save()

# Получение данных пользователя из обновления
def getUser(r: dict):
    id = username = first_name = last_name = ""
    if "message" in r and "id" in r["message"]["from"]:
        id = r["message"]["from"]["id"]
    if "message" in r and "username" in r["message"]["from"]:
        username = r["message"]["from"]["username"]
    if "message" in r and "first_name" in r["message"]["from"]:
        first_name = r["message"]["from"]["first_name"]
    if "message" in r and "last_name" in r["message"]["from"]:
        last_name = r["message"]["from"]["last_name"]
    return {
        "id": id,
        "username": username,
        "first_name": first_name,
        "last_name": last_name,
    }

# Получение сообщения и id из обновления
def getUpdate(r: dict):
    if "message" in r:
        id = r["message"]["from"]["id"]
    else:
        id = ""

    if "message" in r and "text" in r["message"]:
        text = r["message"]["text"]
    else:
        text = ""
    return {"id": id, "text": text}
