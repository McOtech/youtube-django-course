from django.contrib import admin

from upload.models import UploadedFile


class MovieAdmin(admin.ModelAdmin):
    readonly_fields = ("id",)


admin.site.register(UploadedFile, MovieAdmin)
