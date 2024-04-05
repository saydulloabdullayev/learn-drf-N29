from django.db import models


# Create your models here.
class Genre(models.Model):
    genre_name = models.CharField(max_length=255)

    def __str__(self):
        return self.genre_name

    class Meta:
        verbose_name_plural = 'Genres'
        verbose_name = 'Genre'
        db_table = 'genres'


class Movie(models.Model):
    movie_name = models.CharField(max_length=255)
    movie_year = models.IntegerField()
    movie_director = models.CharField(max_length=255)
    movie_rating = models.FloatField()
    movie_genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    movie_banner = models.ImageField(upload_to='movies/')
    movie_url = models.URLField()
    movie_description = models.CharField(max_length=500)

    def __str__(self):
        return self.movie_name

    class Meta:
        db_table = 'movies'
        verbose_name = 'Movie'
        verbose_name_plural = 'Movies'