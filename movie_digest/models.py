from django.db import models


# Model with list of movies and their ids
class dim_movie(models.Model):
    class Meta:
        db_table = 'DimMovie'   # Table name in database
        managed = True         # Allow migrations to be applied

    movie_id = models.IntegerField('movie_id', primary_key=True)
    movie = models.TextField('movie_name', max_length=100, blank=False, null=True)


# Model with genres and their ids
class dim_genre(models.Model):
    class Meta:
        db_table = 'DimGenre'
        managed = True

    genre_id = models.IntegerField('genre_id', primary_key=True)
    genre = models.TextField('genre', max_length=100, blank=True, null=True)


# Model with Cities and their ids
class dim_city(models.Model):
    class Meta:
        db_table = 'DimCity'
        managed = True

    city_id = models.IntegerField('city_id', primary_key=True)
    city = models.TextField('city', max_length=100, blank=True, null=True)


# Model with movie and related details like release date, genre, movie length, etc.
class movie_details(models.Model):
    class Meta:
        db_table = 'MovieDetails'
        # Constraint  - combination of movie, release date and city should be unique
        unique_together = ('movie_fk', 'city_fk','release_date')
        managed = True

    movie_fk = models.ForeignKey('dim_movie', on_delete=models.CASCADE, db_column='movie_fk',
                                 related_name='movie_fk', null=True)
    release_date = models.DateTimeField(auto_now=False, db_column='release_date', null=True)
    genre_fk = models.ForeignKey('dim_genre', on_delete=models.CASCADE, db_column='genre_fk',
                                 related_name='genre_fk', null=True)
    city_fk = models.ForeignKey('dim_city', on_delete=models.CASCADE, db_column='city_fk',
                                related_name='city_fk', null=True)
    movie_director = models.TextField('movie_director', max_length=100, blank=True, null=True)
    # movie_run_time = models.TextField('movie_run_time', max_length=100, blank=True, null=True)
    movie_length = models.TextField('movie_length', max_length=100, blank=True, null=True)

