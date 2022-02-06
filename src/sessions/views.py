from rest_framework import viewsets, status
from rest_framework.response import Response

from .serializers import SessionKeySerializer, SessionDataSerializer
from .services import *


class SessionsViewSet(viewsets.ViewSet):
    def create(self, request):
        session = create_session()
        return Response(SessionKeySerializer(session).data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        session = get_session(pk)
        if session:
            return Response(SessionDataSerializer(session.get_decoded()).data)
        return Response(status=status.HTTP_404_NOT_FOUND)
