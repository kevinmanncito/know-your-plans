from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', include('apps.core.urls'), name='home'),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^app/', include('apps.frontend.urls'), name='frontend'),
    url(r'^rest/', include('apps.rest.urls'), name='rest'),
)
