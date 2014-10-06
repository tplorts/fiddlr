#from django.shortcuts import render
from django.views.generic import TemplateView

from rest_framework import viewsets

from fiddlr import settings
from fwa.models import Artist, Venue, Event, Product
from fwa.serializers import (ArtistSerializer, VenueSerializer, EventSerializer,
                             ProductSerializer)



class Wiew(TemplateView):
    template = 'base'

    def get_context_data(self, **kwargs):
        context = super(Wiew, self).get_context_data(**kwargs)
        if 'ngScopeVars' in context:
            context['ngScopeInitials'] = {}
            for symbol in context['ngScopeVars']:
                if symbol in context:
                    context['ngScopeInitials'].update({
                        symbol: context[symbol],
                    })
        context.update({
            'isProduction': settings.isProduction,
            'useLESS': False,  # Autocompiling LESS these days
            'GoogleAPIKey': settings.GOOGLE_API_KEY,
        })
        return context

    def get_template_names(self):
        return [self.template + '.djt']


########################################################################


class ArtistViewSet(viewsets.ModelViewSet):
    # pylint: disable=no-member
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer


class VenueViewSet(viewsets.ModelViewSet):
    # pylint: disable=no-member
    queryset = Venue.objects.all()
    serializer_class = VenueSerializer


class EventViewSet(viewsets.ModelViewSet):
    # pylint: disable=no-member
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class ProductViewSet(viewsets.ModelViewSet):
    # pylint: disable=no-member
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
