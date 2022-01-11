import string
from random import choices

ROOM_KEY_RESOURCE = string.ascii_uppercase \
                       + string.ascii_lowercase \
                       + '0123456789_-'


def generate_room_key(length: int) -> str:
    return ''.join(choices(ROOM_KEY_RESOURCE, k=length))
