from functools import wraps
from random import choice

from django.conf import settings
from django.core.cache import cache


def handle_unsaved_session(func):
    """
    Saves a new user session if there isn't one already
    """

    @wraps(func)
    def inner_function(*args, **kwargs):
        request = args[1]
        if not request.session.session_key:
            request.session.save()

        return func(*args, **kwargs)

    return inner_function


def set_random_session_data(func):
    """
    Sets the username and color of the django SessionStore if it doesn't exist
    """

    @wraps(func)
    def inner_function(*args, **kwargs):
        request = args[1]
        if 'nickname' not in request.session:
            request.session['nickname'] = choice(cache.get(settings.USERNAMES_CACHE_NAME))
        if 'color' not in request.session:
            request.session['color'] = choice(cache.get(settings.USER_COLORS_CACHE_NAME))

        return func(*args, **kwargs)

    return inner_function
