from django.conf import settings
from django.db import models


class Room(models.Model):
    class Meta:
        db_table = "rooms"

    key = models.CharField(max_length=settings.ROOM_KEY_LENGTH, unique=True, primary_key=True)
    public = models.BooleanField(default=False)
    host = models.CharField(max_length=32)

    def __str__(self):
        return self.key


class RoomMember(models.Model):
    class Meta:
        db_table = "roommembers"

    _id = models.CharField(primary_key=True, max_length=100)
    room_id = models.CharField(max_length=settings.ROOM_KEY_LENGTH)
    nickname = models.CharField(max_length=30)
    color = models.CharField(max_length=7)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.nickname} add to {self.room_id} room'
