import uuid
from django.db.models import CharField, IntegerField, UUIDField, ImageField, FileField, ManyToManyField, ForeignKey, \
    CASCADE

from apps.music.utils import song_cover_path, song_file_path, album_cover_path
from apps.shared.models import AbstractModel


class Genre(AbstractModel):
    name = CharField(max_length=128)


class Artist(AbstractModel):
    id = UUIDField(default=uuid.uuid4().hex, primary_key=True)
    avatar = ImageField(upload_to='artist/%Y/%m/%d', default='avatar.jpeg')
    fullname = CharField(max_length=128)
    followers = IntegerField(default=0)


class Song(AbstractModel):
    title = CharField(max_length=128)
    cover = ImageField(upload_to=song_cover_path)
    file = FileField(upload_to=song_file_path)
    genres = ManyToManyField('music.Genre', 'songs')


class Album(AbstractModel):
    title = CharField(max_length=128)
    author = ForeignKey('music.Artist', CASCADE)
    cover = ImageField(upload_to=album_cover_path)
    songs = ManyToManyField('music.Song')
