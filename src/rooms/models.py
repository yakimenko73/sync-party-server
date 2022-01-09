from django.db import models
from django.conf import settings


class Room(models.Model):
    number = models.CharField(max_length=settings.ROOM_NUMBER_LENGTH, unique=True)

    def __str__(self):
        return self.number
