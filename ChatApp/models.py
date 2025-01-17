from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Room(models.Model):
    room_name = models.CharField(max_length=255)

    def __str__(self):
        return self.room_name
    
    def return_room_messages(self):
        from ChatApp.models import Message

        return Message.objects.filter(room=self)
    
    def create_new_room_message(self, sender, message):

        new_message = Message(room=self, sender=sender, message=message)
        new_message.save()

class Message(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    sender = models.ForeignKey(User, on_delete=models.CASCADE)  # Link to the User model
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sender.username}: {self.message}"
    
# class Message(models.Model):
#     room = models.ForeignKey(Room, on_delete=models.CASCADE)
#     sender = models.CharField(max_length=255)
#     message = models.TextField()

#     def __str__(self):
#         return str(self.room)
