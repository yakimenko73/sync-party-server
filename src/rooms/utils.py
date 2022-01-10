import string
from random import choices

ROOM_NUMBER_RESOURCE = string.ascii_uppercase \
                       + string.ascii_lowercase \
                       + '0123456789_-'


def generate_room_number(length: int) -> str:
    return ''.join(choices(ROOM_NUMBER_RESOURCE, k=length))
