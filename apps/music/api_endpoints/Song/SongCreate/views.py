from rest_framework.generics import CreateAPIView

from apps.music.api_endpoints.Song.SongCreate.serailizers import SongCreateSerializer
from apps.music.models import Song


class SongCreateView(CreateAPIView):
    queryset = Song.objects.all()
    serializer_class = SongCreateSerializer


__all__ = ('SongCreateView',)
