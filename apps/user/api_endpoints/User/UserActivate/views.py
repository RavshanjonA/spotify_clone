from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.user.models import User


class UserActivateView(APIView):
    def get(self, request, token):
        user = get_object_or_404(User, token=token)
        user.is_active = True
        user.save()
        return Response(data={'detail': 'User successfully activated'})


__all__ = ["UserActivateView", ]
