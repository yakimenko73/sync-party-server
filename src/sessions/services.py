from django.contrib.sessions.backends.db import SessionStore


def create_session():
    session = SessionStore()
    session.create()
    return session
