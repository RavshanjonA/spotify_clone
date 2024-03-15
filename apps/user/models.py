from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import ImageField, URLField, OneToOneField, EmailField, DateField, TextChoices, CharField, \
    ForeignKey, ManyToManyField, CASCADE

from apps.shared.models import AbstractModel
from apps.user.managers import UserManager


class UserGender(TextChoices):
    MALE = 'M', 'male'
    FEMALE = 'F', 'female'


class User(AbstractUser):
    avatar = ImageField(upload_to='user/%Y/%m/%d')
    email = None
    followings = ManyToManyField('self', symmetrical=False, related_name='followers', blank=True)
    EMAIL_FIELD = None
    REQUIRED_FIELDS = []
    manager = UserManager()


class UserProfile(AbstractModel):
    user = OneToOneField("user.User", CASCADE)
    email = EmailField(unique=True)
    birthdate = DateField()
    gender = CharField(max_length=6, choices=UserGender.choices)
    country = CharField(max_length=32)

    def follow(self, user):
        self.user.followings.add(user)

    def unfollow(self, user):
        self.user.followings.remove(user)


class Playlist(AbstractModel):
    owner = ForeignKey('user.User', CASCADE)
    title = CharField(max_length=128)
    musics = ManyToManyField('music.Song')
