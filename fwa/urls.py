from django.conf.urls import patterns, url, include

from rest_framework import routers

from fwa.views import (Wiew, ArtistViewSet, VenueViewSet, EventViewSet,
                       ProductViewSet)


# pylint: disable=invalid-name

router = routers.DefaultRouter()
router.register(r'artists', ArtistViewSet)
router.register(r'venues', VenueViewSet)
router.register(r'events', EventViewSet)
router.register(r'products', ProductViewSet)


urlpatterns = patterns(
    '',
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
    url(r'^$', Wiew.as_view(template='portal'), name='portal'),
)
