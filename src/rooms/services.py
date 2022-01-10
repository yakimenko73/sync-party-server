from .models import Room


def get_rooms(public: bool):
    rooms = Room.objects.filter(public__in=[public])
    return rooms


def get_room_by_number(number: str):
    room = Room.objects.filter(number=number).first()
    return room
