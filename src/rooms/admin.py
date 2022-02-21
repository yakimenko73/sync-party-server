from django.contrib import admin

from .models import Room, RoomMember


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('key', 'host', 'public',)
    search_fields = ('key',)
    # not working due to broken parsing SQL to MongoDB query
    list_filter = ('public',)


@admin.register(RoomMember)
class RoomMemberAdmin(admin.ModelAdmin):
    list_display = ('_id', 'room_id', 'nickname', 'color', 'date',)
    search_fields = ('room_id', 'nickname', 'date',)
    list_filter = ('date',)
    readonly_fields = ('_id', 'room_id',)
