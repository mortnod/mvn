from django.conf.urls import patterns, include, url
from django.views.generic.simple import direct_to_template
from django.conf import settings
from django.views.generic.simple import redirect_to

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mvn.views.home', name='home'),
    # url(r'^mvn/', include('mvn.foo.urls')),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', 'blog.views.index', name='blog'),
    (r'^bilder/', include('photos.urls')),
    url(r'^musikk/$', 'music.views.index', name='music'),
    url(r'ommeg/$', 'about.views.index', name='about'),
    (r'feed/$', redirect_to, {'url': 'http://www.youtube.com/watch?v=oHg5SJYRHA0'}),
)

if settings.DEBUG:
    urlpatterns += patterns('',
         url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
            }),
    )
