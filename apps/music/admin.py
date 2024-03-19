from django.contrib import admin

from apps.music.models import Song, Artist, Genre, Album

admin.site.register([Song, Album, Genre])


@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    fields = ["avatar", "fullname"]
    list_display = ["fullname", "avatar", "followers", "id"]
