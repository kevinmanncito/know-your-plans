from django.conf.urls import patterns, include, url

from rest_framework import routers

from .views import MemberViewSet

# Automatic url configuring. New in django-restframework 3.0
router = routers.DefaultRouter()
router.register(r'members', MemberViewSet)

urlpatterns = patterns('',
    url(r'', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
)