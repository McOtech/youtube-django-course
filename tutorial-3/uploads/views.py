from django.http import Http404
from django.shortcuts import render
from uploads.models import Movie


def movie(request, id):
    movie = Movie.objects.get(pk=id)
    if movie is not None:
        return render(request, "movies/movie.html", {"movie": movie})
    else:
        raise Http404("Movie does not exists")
