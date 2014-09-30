from django.conf.urls import patterns, url
from fwa.views import Wiew

urlpatterns = patterns(
    '',
    url(r'^$', Wiew.as_view(template='portal'), name='portal'),
)
