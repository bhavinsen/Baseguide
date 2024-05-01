from rest_framework import serializers
from user_profile.models.artist import Artist


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = '__all__'