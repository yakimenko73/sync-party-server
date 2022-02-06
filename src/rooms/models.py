from django.conf import settings
from django.db import models


class Room(models.Model):
    key = models.CharField(max_length=settings.ROOM_KEY_LENGTH, unique=True, primary_key=True)
    public = models.BooleanField(default=False)
    host = models.CharField(max_length=32)

    def __str__(self):
        return self.key
