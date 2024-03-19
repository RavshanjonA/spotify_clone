from rest_framework.fields import UUIDField
from rest_framework.serializers import Serializer


class ArtistIdSerializer(Serializer):

    artistId = UUIDField()
