from rest_framework.generics import ListAPIView

from apps.music.api_endpoints.Song.SongList.serializers import SongListSerializer
from apps.music.models import Song


class SongListView(ListAPIView):
    queryset = Song.objects.all()
    serializer_class = SongListSerializer


__all__ = ['SongListView', ]
