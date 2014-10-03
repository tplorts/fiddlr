from rest_framework import serializers

from fwa.models import Artist


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ('id', 'title', 'brief', 'lengthy',
                  'picture', 'public', 'editors', 'followers',
                  'website', 'email', 'phone', 'logo',
                  'official', 'categories', 'area')
