import json

from django.conf import settings
from django.core.cache import cache


def init_usernames_cache():
    with open(f"{settings.STATIC_ROOT}/userNames.json", "r") as f:
        usernames = json.load(f)
        cache.set(settings.USERNAMES_CACHE_NAME, usernames["names"])


def init_user_colors_cache():
    with open(f"{settings.STATIC_ROOT}/userColors.json", "r") as f:
        colors = json.load(f)
        cache.set(settings.USER_COLORS_CACHE_NAME, list(colors.values()))
