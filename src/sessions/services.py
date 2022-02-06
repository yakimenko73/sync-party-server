from django.contrib.sessions.backends.db import SessionStore
from django.contrib.sessions.models import Session


def create_session() -> SessionStore:
    session = SessionStore()
    session.create()
    return session


def get_session(session_key: str) -> Session:
    session = Session.objects.filter(pk=session_key).first()
    return session

