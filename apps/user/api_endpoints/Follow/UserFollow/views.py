from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import APIException
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.user.api_endpoints.Follow.UserFollow.serailizers import FollowSerializer
from apps.user.models import User


class UserFollowView(APIView):
    permission_classes = [
        IsAuthenticated,
    ]

    def post(self, request):
        user = request.user
        serializer = FollowSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user_id = serializer.validated_data["userid"]
        if user_id == user.id:
            raise APIException("user can not follow for yourself")
        following_user = self.get_follow_user(user_id=user_id)
        self.follow_to_user(user, following_user)
        return Response(
            data={"detail": "Successfully followed"}, status=status.HTTP_202_ACCEPTED
        )

    def get_follow_user(self, user_id) -> User:
        user = get_object_or_404(User, id=user_id)
        return user

    def follow_to_user(self, user, following_user):
        if following_user in user.followings.all():
            raise APIException("You are already following")
        else:
            user.userprofile.follow(following_user)
            user.save()


__all__ = [
    "UserFollowView",
]
