from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from apps.music.api_endpoints.Artist.ArtistList.serailizers import ArtistListSerializer
from apps.music.models import Artist


class ArtistListView(ListAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistListSerializer
    authentication_classes = [JWTAuthentication, ]
    permission_classes = [IsAuthenticated,]


__all__ = ('ArtistListView',)
