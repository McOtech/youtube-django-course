from django.db import models


class Movie(models.Model):
    name = models.CharField(max_length=300)
    image = models.ImageField(upload_to="files/covers")


class File(models.Model):
    tag = models.CharField(max_length=300)
    path = models.FileField(upload_to="files/archives")
