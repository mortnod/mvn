from django.conf.urls import patterns, include, url
from django.views.generic.simple import direct_to_template

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
    url(r'^musikk/$', direct_to_template, {'template': 'music/music.html'}),
)
