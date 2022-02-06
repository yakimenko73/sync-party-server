from django.contrib import admin

from .models import Room


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('key', 'host', 'public',)
    search_fields = ('key',)
    list_filter = ('public',)  # not working due to broken parsing SQL to MongoDB query
