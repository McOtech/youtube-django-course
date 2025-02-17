from django.contrib import admin
from .models import File, Movie


class MovieAdmin(admin.ModelAdmin):
    readonly_fields = ("id",)


admin.site.register(Movie, MovieAdmin)
admin.site.register(File, MovieAdmin)
