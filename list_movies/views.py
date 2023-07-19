from django.shortcuts import render
from django.db.models import Q
from .models import Movie, Genre

def movie_list(request):
    genres = Genre.objects.values_list('name', flat=True).distinct()
    movies = Movie.objects.all()

    selected_genres = request.GET.getlist('genre')  # Get selected genres from query parameters
    search_query = request.GET.get('q')  # Get search query from query parameters
    sort_by = request.GET.get('sort')  # Get the sorting parameter from the query parameters


    # Apply genre filter
    if selected_genres:
        genre_filters = Q(genres__name__in=selected_genres)
        movies = movies.filter(genre_filters)

    # Apply search filter
    if search_query:
        movies = movies.filter(title__icontains=search_query)
    
    # Apply sorting
    if sort_by:
        if sort_by.startswith('-'):
            sort_field = sort_by[1:]  
            movies = movies.order_by(f'-{sort_field}')
        else:
            movies = movies.order_by(sort_by)

    context = {
        'movies': movies,
        'genres': genres,
        'selected_genres': selected_genres,
        'search_query': search_query,
        'sort_by': sort_by,
    }

    return render(request, 'list.html', context)
