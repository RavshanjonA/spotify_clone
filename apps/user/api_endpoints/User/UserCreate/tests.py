import json

from django.core.files import File
from django.urls import reverse
from rest_framework.test import APITestCase

from apps.user.models import User


class UserCreateTest(APITestCase):
    def setUp(self):
        pass
    def test_user_create(self):
        url = reverse("user-create")
        data = {
            "username": "test",
            "first_name": "Test",
            "last_name": "Test1",
            "password1": "test1",
            "password2": "test1",
            "email": "user@gmail.com",
            "avatar": open("media/avatar.jpeg", "rb")
        }
        response = self.client.post(url, data)
        user = User.objects.get(id=1)
        data = json.loads(response.content)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(data["username"], user.username)
