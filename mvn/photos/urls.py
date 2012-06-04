from django.conf.urls.defaults import *

urlpatterns = patterns('photos.views',
    url(r'^$', 'index', name='index'),
    url(r'album/(?P<album_id>\d+)/$', 'album', name='album'),
)