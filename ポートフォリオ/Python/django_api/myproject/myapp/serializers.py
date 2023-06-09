from rest_framework import serializers
from .models import Artist

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ['id', 'name', 'discography', 'debut_date', 'agency', 'genre']