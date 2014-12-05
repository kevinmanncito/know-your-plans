from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',

    url(r'^$', include('apps.core.urls'), name='home'),
    url(r'^app$', include('apps.frontend.urls'), name='frontend'),

    url(r'^admin/', include(admin.site.urls)),

)
