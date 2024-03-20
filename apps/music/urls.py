from django.urls import path

from apps.music.api_endpoints.Artist import ArtistListView, ArtistCreateView, ArtistRetrieveUpdateDestroyView
from apps.music.api_endpoints.Song import SongCreateView, SongListView, SongRetrieveUpdateDestroyView

urlpatterns = [
    path("song/create", SongCreateView.as_view()),
    path("song/", SongListView.as_view()),
    path("song/<pk>/", SongRetrieveUpdateDestroyView.as_view()),
    path("artist/", ArtistListView.as_view()),
    path("artist/create", ArtistCreateView.as_view()),
    path("artist/<pk>", ArtistRetrieveUpdateDestroyView.as_view()),
]