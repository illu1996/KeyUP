from django.contrib import admin
from .models import Genre, Keyword, Movie, Review
# Register your models here.
admin.site.register(Genre)
admin.site.register(Keyword)

admin.site.register(Review)


class FamilyAdmin(admin.ModelAdmin):
    search_fields = ['title']
    
admin.site.register(Movie, FamilyAdmin)