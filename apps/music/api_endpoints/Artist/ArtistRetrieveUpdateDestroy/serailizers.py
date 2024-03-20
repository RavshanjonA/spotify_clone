from rest_framework.fields import DateTimeField
from rest_framework.serializers import ModelSerializer

from apps.music.models import Artist


class ArtistRetrieveUpdateDestroySerailizer(ModelSerializer):
    created_at = DateTimeField(read_only=True)
    class Meta:
        model = Artist
        fields = ('id', 'avatar', 'fullname', 'followers', "created_at")
