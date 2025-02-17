import os
from django.http import FileResponse, Http404
from django.shortcuts import render
from uploads import settings
from uploads.models import File, Movie


def movie(request, id):
    movie = Movie.objects.get(pk=id)
    if movie is not None:
        return render(request, "movies/movie.html", {"movie": movie})
    else:
        raise Http404("Movie does not exists")


def download_file(request, id):
    file_object = File.objects.get(pk=id)
    if file_object is not None:
        # try:
        path = os.path.join(settings.BASE_DIR, str(file_object.path))
        file = open(path, "rb")
        return FileResponse(file, as_attachment=True)
        # except error:
        #     print(file_object.path)
        #     raise Http404("Error while trying to download the file")
    else:
        raise Http404("File does not exists")
