from rest_framework.generics import CreateAPIView
from rest_framework.parsers import FileUploadParser, FormParser, MultiPartParser, JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.user.api_endpoints.User.UserCreate.serializers import UserCreateSerializer
from apps.user.models import User


class UserCreateView(APIView):
    def post(self, request):
        serailizer = UserCreateSerializer(data=request.data)
        serailizer.avatar = request.FILES['avatar']
        serailizer.is_valid(raise_exception=True)
        serailizer.save()
        return Response(data={'detail': "Check your inbox we have sent an activation link"})
    # queryset = User.objects.all()
    # serializer_class = UserCreateSerializer
    # parser_classes = [MultiPartParser, FormParser, JSONParser]


__all__ = ('UserCreateView',)
