from django.db import models


class Director(models.Model):
    name = models.CharField(max_length=128, db_index=True)

class Genre(models.Model):
    name = models.CharField(max_length=128, db_index=True)

class Movie(models.Model):
    name = models.CharField(max_length=128, db_index=True)
    director = models.ForeignKey(Director)
    genre = models.ManyToManyField(Genre)
    imdb_score = models.FloatField(default=-1)
    popularity = models.FloatField(default=-1)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = (("name", "director", "imdb_score"),)
