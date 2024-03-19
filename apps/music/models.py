import uuid
from django.db.models import (
    CharField,
    IntegerField,
    UUIDField,
    ImageField,
    FileField,
    ManyToManyField,
    ForeignKey,
    CASCADE,
    DO_NOTHING,
)

from apps.music.utils import song_cover_path, song_file_path, album_cover_path
from apps.shared.models import AbstractModel


class Genre(AbstractModel):
    name = CharField(max_length=128)

    def __str__(self):
        return self.name


class Artist(AbstractModel):
    id = UUIDField(primary_key=True)
    avatar = ImageField(upload_to="artist/%Y/%m/%d", default="avatar.jpeg")
    fullname = CharField(max_length=128)
    followers = IntegerField(default=0)

    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        if not self.id:
            self.id = uuid.uuid4()
        super().save(force_insert, force_update, using, update_fields)

    def __str__(self):
        return self.fullname


class Album(AbstractModel):
    title = CharField(max_length=128)
    author = ForeignKey("music.Artist", CASCADE)
    cover = ImageField(upload_to=album_cover_path)

    def __str__(self):
        return self.title


class Song(AbstractModel):
    title = CharField(max_length=128)
    cover = ImageField(upload_to=song_cover_path)
    file = FileField(upload_to=song_file_path)
    genres = ManyToManyField("music.Genre", "songs")
    album = ForeignKey("music.Album", DO_NOTHING, "songs")

    def __str__(self):
        return self.title
