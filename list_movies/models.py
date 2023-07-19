from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self) -> str:
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=255)
    poster = models.ImageField(upload_to='posters/')
    genres = models.ManyToManyField(Genre)
    rating = models.CharField(max_length=10)
    year_release = models.IntegerField()
    metacritic_rating = models.IntegerField()
    runtime = models.CharField(max_length=10)

