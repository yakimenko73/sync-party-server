from django.conf import settings
from django.db.models import QuerySet

from .models import Room, RoomMember
from .utils import generate_room_key


def get_rooms(public: bool) -> QuerySet:
    rooms = Room.objects.filter(public__in=[public]).iterator()
    return rooms


def get_room_by_key(key: str) -> QuerySet:
    room = Room.objects.filter(key=key).first()
    return room


def create_room(host: str) -> Room:
    room = Room(
        key=generate_room_key(settings.ROOM_KEY_LENGTH),
        host=host
    )
    room.save()
    return room


def get_room_members(room_key: str) -> [RoomMember]:
    members = RoomMember.objects.filter(room_id=room_key).iterator()
    return members
