from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
import requests


def set_webhook():
    response = requests.post(f"{settings.TELEGRAM_URL}{settings.TOKEN}/deleteWebhook")
    response = requests.get(
        f"{settings.TELEGRAM_URL}{settings.TOKEN}/setWebhook?url={settings.WEBHOOK_URL}"
    )


class Command(BaseCommand):
    help = "Set webhook"

    def handle(self, *args, **options):
        set_webhook()
        print("OK")
