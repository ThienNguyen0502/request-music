from django.contrib import admin
from music_online.models import Song


class SongAdmin(admin.ModelAdmin):
    list_display = ('song_name', 'source', 'sender', 'pub_date')
    list_filter = ['sender', 'pub_date']
    search_fields = ['song_name']

admin.site.register(Song, SongAdmin)
