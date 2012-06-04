from blog.models import Entry, Image, File, Youtube
from django.contrib import admin
import models

class CommonMedia:
  js = (
    'http://ajax.googleapis.com/ajax/libs/dojo/1.7.2/dojo/dojo.js',
    '/static/base/scripts/dojo_settings.js',
  )
  css = {
    'all': ('/static/base/css/dojo_css.css',),
  }

class ImageInline(admin.TabularInline):
    model = Image
    extra = 4
    
class FileInline(admin.StackedInline):
    model = File
    extra = 1
    
class YoutubeInline(admin.StackedInline):
    model = Youtube
    extra = 1

class EntryAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['headline', 'body']}),
    ]
    inlines = [ImageInline, FileInline, YoutubeInline]

admin.site.register(Entry, EntryAdmin, Media = CommonMedia)
