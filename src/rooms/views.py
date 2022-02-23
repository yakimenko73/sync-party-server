from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from user_sessions.decorators import set_random_session_data, handle_unsaved_session
from .serializers import RoomSerializer, RoomMembersSerializer
from .services import *


class RoomViewSet(viewsets.ViewSet):
    def list(self, _request):
        rooms = get_rooms(public=True)
        return Response(RoomSerializer(rooms, many=True).data)

    def retrieve(self, _request, pk=None):
        room = get_room_by_key(pk)
        if room:
            return Response(RoomSerializer(room).data)
        return Response(status=status.HTTP_404_NOT_FOUND)

    @handle_unsaved_session
    @set_random_session_data
    def create(self, request):
        room = create_room(request.session.session_key)
        return Response(RoomSerializer(room).data, status=status.HTTP_201_CREATED)

    @handle_unsaved_session
    @set_random_session_data
    @action(detail=True, methods=['get'])
    def members(self, _request, pk=None):
        print(_request)
        if not get_room_by_key(pk):
            return Response(status=status.HTTP_404_NOT_FOUND)

        members = get_room_members(pk)
        return Response(RoomMembersSerializer(members, many=True).data, status=status.HTTP_200_OK)
