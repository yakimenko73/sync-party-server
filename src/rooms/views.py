from rest_framework import viewsets, status
from rest_framework.response import Response

from sessions.decorators import handle_unsaved_session
from .serializers import RoomSerializer
from .services import *


class RoomViewSet(viewsets.ViewSet):
    def list(self, request):
        rooms = get_rooms(public=True)
        return Response(RoomSerializer(rooms, many=True).data)

    @handle_unsaved_session
    def retrieve(self, request, pk=None):
        room = get_room_by_number(pk)
        if room:
            return Response(RoomSerializer(room).data)
        return Response(status=status.HTTP_404_NOT_FOUND)

    @handle_unsaved_session
    def create(self, request):
        room = create_room()
        return Response(RoomSerializer(room).data)
