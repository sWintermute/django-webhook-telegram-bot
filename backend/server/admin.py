from django.contrib import admin
from django.contrib.admin.decorators import register

from .models import Events, Users


class EventsAdmin(admin.ModelAdmin):
    list_display = ("date", "title", "body")
    search_fields = ("date", "title")

class UsersAdmin(admin.ModelAdmin):
    list_display = ("chatId", "firstName", "lastName", "username")


admin.site.register(Events, EventsAdmin)
admin.site.register(Users, UsersAdmin)

