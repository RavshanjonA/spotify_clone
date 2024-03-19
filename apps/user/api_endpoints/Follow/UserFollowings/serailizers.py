from rest_framework.serializers import ModelSerializer

from apps.user.models import User


class FollowingListSerailizer(ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "avatar")
