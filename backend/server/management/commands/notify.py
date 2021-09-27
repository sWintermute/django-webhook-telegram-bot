from django.core.management.base import BaseCommand, CommandError
from server.models import Events, Users

from datetime import date
from server.views import dataExtractor, TelegramBotView


def notify():
    usersList = Users.objects.all()
    today = date.today()
    today_filter = Events.objects.filter(date__month=today.month, date__day=today.day)
    for u in usersList:
        for e in today_filter:
            s = dataExtractor(e)
            TelegramBotView.send_message(s, u.chatId)


class Command(BaseCommand):
    help = "Custom management commands"

    def handle(self, *args, **options):
        notify()
        print("OK")
