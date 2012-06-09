from django.contrib import admin
from music.models import MusicAlbum, Song, CoverPhoto

class SongInline(admin.StackedInline):
    model = Song
    extra = 5

class CoverPhotoInline(admin.StackedInline):
    model = CoverPhoto
    extra = 3

class MusicAlbumAdmin(admin.ModelAdmin):
    fieldsets = [
            (None, {'fields': ['name']}),
                ]
    inlines = [SongInline, CoverPhotoInline]

admin.site.register(MusicAlbum, MusicAlbumAdmin)
