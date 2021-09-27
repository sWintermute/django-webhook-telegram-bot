from django.urls import path


from .views import TelegramBotView
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    path("", csrf_exempt(TelegramBotView.as_view())),
]
