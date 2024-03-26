from rest_framework_simplejwt.views import TokenObtainPairView

from apps.user.serailizers import MyTokenObtainPairSerializer


class MyCustomObtainTokenView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
