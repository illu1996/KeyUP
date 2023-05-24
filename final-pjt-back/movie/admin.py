from django.contrib import admin
from .models import Genre, Keyword, Movie, Review
# Register your models here.
admin.site.register(Genre)
admin.site.register(Keyword)
admin.site.register(Movie)
admin.site.register(Review)