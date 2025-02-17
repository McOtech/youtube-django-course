# multiuploader/forms.py
from django import forms
from .models import UploadedFiles


class MultipleFileUploadForm(forms.ModelForm):
    class Meta:
        model = UploadedFiles
        fields = ["file1", "file2", "file3"]

    def clean(self):
        cleaned_data = super().clean()
        # for field_name in ['file1', 'file2', 'file3']:
        #     file = cleaned_data.get(field_name)
        #     if file:
        #         if file.size > 5 * 1024 * 1024:  # 5 MB limit
        #             self.add_error(field_name, f"{field_name} size must be under 5 MB.")
        #     else:
        #         self.add_error(field_name, f"{field_name} is required.")
        return cleaned_data
