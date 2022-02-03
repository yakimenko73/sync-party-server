from rest_framework import viewsets, status
from rest_framework.response import Response

from .serializers import SessionSerializer
from .services import *


class SessionsViewSet(viewsets.ViewSet):
    def create(self, request):
        session = create_session()
        return Response(SessionSerializer(session).data, status=status.HTTP_201_CREATED)
