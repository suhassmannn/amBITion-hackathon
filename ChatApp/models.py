from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class ChatRoom(models.Model):
    owner = models.ForeignKey(User, related_name='owned_rooms', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='user_rooms', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)  # Name for identification (optional)

    def _str_(self):
        return f"Chat Room {self.id} - {self.user.username} <-> {self.owner.username}"

class Message(models.Model):
    room = models.ForeignKey(ChatRoom, related_name='messages', on_delete=models.CASCADE)
    sender = models.ForeignKey(User, related_name='sent_messages', on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return f'{self.sender.username} - {self.timestamp}'
