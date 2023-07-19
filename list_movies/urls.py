from django.urls import path
from .views import movie_list

app_name = 'list_movies'

urlpatterns = [
    path('movies/', movie_list, name='movie_list'),
    path('', movie_list, name='movie_list'),
]
