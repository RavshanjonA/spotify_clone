from django.contrib import admin

from apps.user.models import UserProfile, User, Playlist

admin.site.register([UserProfile, User, Playlist])
