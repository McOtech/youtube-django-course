from django.http import HttpResponse
from django.shortcuts import render

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
    return render(request, "movies/movies.html", data)


def home(request):
    return HttpResponse("Home Page")
