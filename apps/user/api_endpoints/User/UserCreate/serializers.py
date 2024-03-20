from rest_framework.exceptions import ValidationError
from rest_framework.fields import EmailField, CharField, ImageField
from rest_framework.serializers import ModelSerializer

from apps.user.models import User


class UserCreateSerializer(ModelSerializer):
    email = EmailField()
    password1 = CharField(max_length=128)
    password2 = CharField(max_length=128)
    first_name = CharField(max_length=128)
    last_name = CharField(max_length=128)
    avatar = ImageField()

    def validate(self, attrs):
        if attrs["password1"] != attrs["password2"]:
            raise ValidationError("password1 and password2 must match")
        return attrs

    def validate_username(self, value):
        if User.objects.filter(username=value).exists():
            raise ValidationError("username already taken")
        return value

    def create(self, validated_data):
        first_name = validated_data.get('first_name')
        last_name = validated_data.get('last_name')
        password = validated_data.get('password1')
        username = validated_data.get('username')
        email = validated_data.get('email')
        avatar = validated_data.get('avatar')
        user = User.objects.create(username=username, first_name=first_name, last_name=last_name, is_active=False,
                                   avatar=avatar)
        user.set_password(password)
        user.save()
        user.userprofile.email = email
        user.save()
        validated_data["avatar"] = str(user.avatar.url)
        return validated_data

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', "avatar")
