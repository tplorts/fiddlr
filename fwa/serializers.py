from rest_framework import serializers

from fwa.models import Artist, Venue, Event, Product


ENTITY_FIELDS = ('id', 'title', 'brief', 'lengthy', 'picture', 'public',
                 'editors', 'followers')

CREA_FIELDS = ENTITY_FIELDS + ('website', 'email', 'phone', 'logo',
                               'official', 'categories')

PROJECT_FIELDS = ENTITY_FIELDS + ('artist', 'coartists', 'price')


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = CREA_FIELDS + ('area',)


class VenueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venue
        fields = CREA_FIELDS + ('address',)


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = PROJECT_FIELDS + ('venue', 'attendees', 'start', 'end',
                                   'settimes', 'reserve', 'ticket')


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = PROJECT_FIELDS + ('release',)

