from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from apps.user.api_endpoints.Follow import UserFollowView, UserUnfollowView

urlpatterns = [
    path('token/', obtain_auth_token),
    path('user-follow/', UserFollowView.as_view()),
    path('user-unfollow/', UserUnfollowView.as_view()),
]
