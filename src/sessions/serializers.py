from rest_framework import serializers


class SessionSerializer(serializers.BaseSerializer):
    def to_representation(self, instance):
        return {
            'session_key': instance.session_key,
        }
