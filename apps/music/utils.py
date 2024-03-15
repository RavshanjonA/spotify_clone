import uuid

from django.utils import timezone


def song_cover_path(instance, filename):
    current_dt = timezone.now()
    return f'song_cover/{current_dt.strftime("%Y_%m")}/{uuid.uuid4().hex}/{filename}'


def album_cover_path(instance, filename):
    current_dt = timezone.now()
    return f'album_cover/{current_dt.strftime("%Y_%m")}/{uuid.uuid4().hex}/{filename}'


def song_file_path(instance, filename):
    current_dt = timezone.now()
    return f'song_files/{current_dt.strftime("%Y_%m")}/{uuid.uuid4().hex}/{filename}'
