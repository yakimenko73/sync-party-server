from django.contrib.sessions.backends.db import SessionStore
from rest_framework import viewsets, status
from rest_framework.response import Response

from .serializers import SessionSerializer


class SessionsViewSet(viewsets.ViewSet):
    def create(self, request):
        session_store = SessionStore()
        session_store.create()
        return Response(SessionSerializer(session_store.session_key).data, status=status.HTTP_201_CREATED)
