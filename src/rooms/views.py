from rest_framework import viewsets, status
from rest_framework.response import Response

from .serializers import RoomSerializer
from .services import get_rooms, get_room_by_number


class RoomViewSet(viewsets.ViewSet):
    def list(self, request):
        rooms = get_rooms(public=True)
        return Response(RoomSerializer(rooms, many=True).data)

    def retrieve(self, request, pk=None):
        room = get_room_by_number(pk)
        if room:
            return Response(RoomSerializer(room).data)
        return Response(status=status.HTTP_404_NOT_FOUND)
