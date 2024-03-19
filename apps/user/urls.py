from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from apps.user.api_endpoints.Follow import (
    UserFollowView,
    UserUnfollowView,
    UserFollowersView,
    UserFollowingsView,
    UserArtistFollowView,
    UserArtistUnFollowView,
)

urlpatterns = [
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("user-follow/", UserFollowView.as_view()),
    path("user-unfollow/", UserUnfollowView.as_view()),
    path("artist-follow/", UserArtistFollowView.as_view()),
    path("artist-unfollow/", UserArtistUnFollowView.as_view()),
    path("<pk>/followers/", UserFollowersView.as_view()),
    path("<pk>/followings/", UserFollowingsView.as_view()),
]
