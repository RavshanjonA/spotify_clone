from rest_framework.serializers import ModelSerializer

from apps.music.models import Artist


class ArtistCreateSerializer(ModelSerializer):
    class Meta:
        model = Artist
        fields = ('fullname', 'avatar')
