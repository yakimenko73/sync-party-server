from rest_framework import serializers


class SessionSerializer(serializers.BaseSerializer):
    def to_representation(self, session_key):
        return {
            'session_key': session_key,
        }
