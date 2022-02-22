from rest_framework import serializers

from .models import Room, RoomMember


class RoomSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Room
        fields = ('key', 'public',)


class RoomMembersSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.CharField(source='_id')

    class Meta:
        model = RoomMember
        fields = ('id', 'nickname', 'color',)
