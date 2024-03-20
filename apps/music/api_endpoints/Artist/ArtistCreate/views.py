from rest_framework.generics import CreateAPIView

from apps.music.api_endpoints.Artist.ArtistCreate.serailizers import ArtistCreateSerializer
from apps.music.models import Artist


class ArtistCreateView(CreateAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistCreateSerializer


__all__ = ["ArtistCreateView", ]
