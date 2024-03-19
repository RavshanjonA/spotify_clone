from django.db import transaction
from django.shortcuts import get_object_or_404
from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import APIException
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.music.models import Artist
from apps.user.api_endpoints.Follow.UserArtist.serializers import ArtistIdSerializer


class UserArtistFollowView(APIView):
    permission_classes = (IsAuthenticated,)

    @transaction.atomic
    def post(self, request):
        user = self.request.user
        serializer = ArtistIdSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        artist_id = serializer.validated_data["artistId"]
        artist = get_object_or_404(Artist, id=artist_id)
        self.check_user_follow_artist(user, artist)
        artist.followers += 1
        artist.save()
        user.userprofile.follow_artist(artist_id)
        return Response(data={"detail": "user successfully followed artist"})

    def check_user_follow_artist(self, user, artist):
        if artist in user.artist_following.all():
            raise APIException("user already following")


class UserArtistUnFollowView(APIView):
    permission_classes = (IsAuthenticated,)

    @transaction.atomic
    def post(self, request):
        user = self.request.user
        serializer = ArtistIdSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        artist_id = serializer.validated_data["artistId"]
        artist = get_object_or_404(Artist, id=artist_id)
        artist.followers -= 1
        artist.save()
        self.check_user_follow_artist(user, artist)
        user.userprofile.unfollow_artist(artist)
        return Response(data={"detail": "user successfully unfollowed artist"})

    def check_user_follow_artist(self, user, artist):
        if artist not in user.artist_following.all():
            raise APIException("user is not following to artist")


__all__ = ("UserArtistFollowView", "UserArtistUnFollowView")
