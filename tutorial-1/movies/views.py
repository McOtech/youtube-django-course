from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import Movie

data = {
    "movies": [
        {"id": 1, "title": "Movie 1", "year": 1669},
        {"id": 2, "title": "Movie 2", "year": 2000},
        {"id": 3, "title": "Movie 3", "year": 1878},
        {"id": 4, "title": "Movie 4", "year": 2015},
        {"id": 5, "title": "Movie 5", "year": 2024},
    ]
}


def movies(request):
    title = request.POST.get("title")
    year = request.POST.get("year")

    if title and year:
        movie = Movie(title=title, year=year)
        movie.save()
        return HttpResponseRedirect("/movies")

    movies_data = Movie.objects.all()
    return render(request, "movies/movies.html", {"movies": movies_data})


def home(request):
    return HttpResponse("Home Page")


def detail(request, id):
    try:
        movie_data = Movie.objects.get(pk=id)
        return render(request, "movies/detail.html", {"movie": movie_data})
    except:
        raise Http404("Movie does not exists!")


def create(request):
    return render(request, "movies/create.html")


def delete(request, id):
    try:
        movie_data = Movie.objects.get(pk=id)
    except:
        raise Http404("Movie does not exists!")

    movie_data.delete()
    return HttpResponseRedirect("/movies")
