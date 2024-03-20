from rest_framework.serializers import ModelSerializer

from apps.music.models import Artist


class ArtistListSerializer(ModelSerializer):
    class Meta:
        model = Artist
        fields = ('id', 'avatar', 'fullname', 'followers', "created_at")
