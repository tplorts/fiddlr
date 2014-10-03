from django.conf.urls import patterns, url, include

from rest_framework import routers

from fwa.views import Wiew, ArtistViewSet


router = routers.DefaultRouter()
router.register(r'artists', ArtistViewSet)


urlpatterns = patterns(
    '',
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^$', Wiew.as_view(template='portal'), name='portal'),
)
