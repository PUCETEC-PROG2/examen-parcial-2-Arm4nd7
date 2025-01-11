from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path("movies/", views.index, name="index."),
    path('<int:movie_id>/', views.movie, name='movie')
]