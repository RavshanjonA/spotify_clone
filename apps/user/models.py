from django.contrib.auth.models import AbstractUser
from django.db.models import (
    ImageField,
    OneToOneField,
    EmailField,
    DateField,
    TextChoices,
    CharField,
    ForeignKey,
    ManyToManyField,
    CASCADE, BooleanField,
)

from apps.shared.models import AbstractModel
from apps.user.managers import UserManager


class UserGender(TextChoices):
    MALE = "M", "male"
    FEMALE = "F", "female"


class User(AbstractUser):
    avatar = ImageField(upload_to="user/%Y/%m/%d")
    email = None
    followings = ManyToManyField("self", symmetrical=False, related_name="followers")
    artist_following = ManyToManyField(
        "music.Artist",
        "users",
    )
    is_active = BooleanField(default=False)
    token = CharField(max_length=128)
    EMAIL_FIELD = None
    REQUIRED_FIELDS = []
    manager = UserManager()

    def __str__(self):
        return self.username


class UserProfile(AbstractModel):
    user = OneToOneField("user.User", CASCADE)
    email = EmailField(unique=True, null=True, blank=True)
    birthdate = DateField(null=True, blank=True)
    gender = CharField(max_length=6, choices=UserGender.choices, null=True)
    country = CharField(max_length=32, blank=True)

    def follow(self, user):
        self.user.followings.add(user)

    def unfollow(self, user):
        self.user.followings.remove(user)

    def follow_artist(self, artist_id):
        self.user.artist_following.add(artist_id)

    def unfollow_artist(self, artist_id):
        self.user.artist_following.remove(artist_id)

    def __str__(self):
        return f"{self.user.username} {self.gender}"


class Playlist(AbstractModel):
    owner = ForeignKey("user.User", CASCADE)
    title = CharField(max_length=128)
    musics = ManyToManyField("music.Song")
