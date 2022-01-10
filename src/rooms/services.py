from django.conf import settings
from django.db.models import QuerySet

from .models import Room
from .utils import generate_room_number


def get_rooms(public: bool) -> QuerySet:
    rooms = Room.objects.filter(public__in=[public])
    return rooms


def get_room_by_number(number: str) -> QuerySet:
    room = Room.objects.filter(number=number).first()
    return room


def create_room() -> Room:
    room = Room(number=generate_room_number(settings.ROOM_NUMBER_LENGTH))
    room.save()
    return room
