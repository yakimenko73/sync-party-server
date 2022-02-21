from rest_framework import serializers

from .models import Room, RoomMembers


class RoomSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Room
        fields = ('key', 'public',)


class RoomMembersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RoomMembers
        fields = ('nickname', 'color',)
