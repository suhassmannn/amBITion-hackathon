from django.contrib import admin
from ChatApp.models import ChatRoom, Message

admin.site.register(ChatRoom)
admin.site.register(Message)