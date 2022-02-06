from django.contrib import admin
from django.contrib.sessions.models import Session


@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    list_display = (
        'session_key',
        '_session_data',
        'expire_date'
    )
    search_fields = (
        'session_key',
        'expire_date',
    )
    list_filter = ('expire_date',)

    def _session_data(self, obj):
        return obj.get_decoded()
