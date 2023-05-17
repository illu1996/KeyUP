from django.db import models
from django.conf import settings

# Create your models here.
class Movie(models.Model):
    adult = models.BooleanField()
    title = models.TextField()
    original_title = models.TextField()
    genre_id = models.TextField()
    overview = models.TextField()
    poster_path = models.TextField()
    release_data = models.DateField()
    vote_average = models.FloatField()
    vote_count = models.IntegerField()
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_movies')
    

class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

