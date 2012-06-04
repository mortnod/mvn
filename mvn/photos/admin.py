from photos.models import Album, Photo
from django.contrib import admin

class PhotoInline(admin.StackedInline):
    model = Photo
    extra = 10

class AlbumAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name', 'cover']}),
    ]
    inlines = [PhotoInline]


admin.site.register(Album, AlbumAdmin)
