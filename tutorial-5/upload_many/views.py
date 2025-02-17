# multiuploader/views.py
from django.shortcuts import render, redirect
from django.views import View
from .forms import MultipleFileUploadForm


class MultipleFileUploadView(View):
    def get(self, request):
        form = MultipleFileUploadForm()
        return render(request, "uploads/upload.html", {"form": form})

    def post(self, request):
        form = MultipleFileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("upload_success")
        return render(request, "uploads/upload.html", {"form": form})


def upload_success(request):
    return render(request, "uploads/success.html")
