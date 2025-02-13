from django.db import models


class Movie(models.Model):
    name = models.CharField(max_length=300)
    image = models.ImageField(upload_to="files/covers")
