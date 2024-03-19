from rest_framework import status
from rest_framework.generics import (
    RetrieveUpdateDestroyAPIView,
    get_object_or_404,
    ListAPIView,
)
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.user.api_endpoints.Follow.UserFollowers.serializers import (
    FollowerListSerailizer,
)
from apps.user.models import User


class UserFollowersView(ListAPIView):
    serializer_class = FollowerListSerailizer

    def get_queryset(self):
        pk = self.kwargs["pk"]
        user = get_object_or_404(User, pk=pk)
        return user.followers.all()


__all__ = ("UserFollowersView",)
