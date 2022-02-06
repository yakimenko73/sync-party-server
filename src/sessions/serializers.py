from rest_framework import serializers


class SessionKeySerializer(serializers.BaseSerializer):
    def to_representation(self, instance):
        return {
            'session_key': instance.session_key,
        }


class SessionDataSerializer(serializers.BaseSerializer):
    def to_representation(self, instance):
        return instance
