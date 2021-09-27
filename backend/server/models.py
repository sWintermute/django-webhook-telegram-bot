from django.db import models
from django.db.models.deletion import DO_NOTHING
from django.db.models.fields import DateField


class Events(models.Model):
    date = models.DateField(verbose_name="Дата")
    title = models.CharField(verbose_name="Заголовок", max_length=128)
    body = models.TextField(verbose_name="Описание")

    def __str__(self):
        return str(self.date) + " | " + str(self.title)

    class Meta:
        verbose_name_plural = "Список значимых событий"
        ordering = ["date"]

class Users(models.Model):
    chatId = models.CharField(verbose_name="Chat id", max_length=9)
    firstName = models.CharField(verbose_name="First name", max_length=64)
    lastName = models.CharField(verbose_name="Last name", max_length=64)
    username = models.CharField(verbose_name="Username", max_length=64)

    def __str__(self):
        return str(self.firstName) + " " + str(self.lastName) + " " + str(self.chatId)

    class Meta:
        verbose_name_plural = "Пользователи"

