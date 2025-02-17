# multiuploader/models.py
from django.db import models


class UploadedFiles(models.Model):
    file1 = models.FileField(upload_to="uploads/file1/")
    file2 = models.FileField(upload_to="uploads/file2/")
    file3 = models.FileField(upload_to="uploads/file3/")
    uploaded_at = models.DateTimeField(auto_now_add=True)
