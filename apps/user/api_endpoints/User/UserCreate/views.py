from rest_framework.generics import CreateAPIView
from rest_framework.parsers import FileUploadParser

from apps.user.api_endpoints.User.UserCreate.serializers import UserCreateSerializer
from apps.user.models import User


class UserCreateView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer
    # parser_classes = [FileUploadParser, ]


__all__ = ('UserCreateView',)
