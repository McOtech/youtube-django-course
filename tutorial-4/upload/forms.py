from django import forms
from .models import UploadedFile


class FileUploadForm(forms.ModelForm):
    class Meta:
        model = UploadedFile
        fields = ["file"]

    def clean_file(self):
        file = self.cleaned_data.get("file")
        return file
        # if file:
        #     if file.size > 5 * 1024 * 1024:  # 5 MB limit
        #         raise forms.ValidationError("File size must be under 5 MB.")
        #     return file
        # else:
        #     raise forms.ValidationError("Couldn't read uploaded file")
