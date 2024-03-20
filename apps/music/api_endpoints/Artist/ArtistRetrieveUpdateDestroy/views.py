from rest_framework.generics import RetrieveUpdateDestroyAPIView

from apps.music.api_endpoints.Artist.ArtistRetrieveUpdateDestroy.serailizers import \
    ArtistRetrieveUpdateDestroySerailizer
from apps.music.models import Artist


class ArtistRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistRetrieveUpdateDestroySerailizer


__all__ = ('ArtistRetrieveUpdateDestroyView',)
