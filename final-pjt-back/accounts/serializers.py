from rest_framework import serializers
from .models import User
from movie.models import Movie


class UserSerializer(serializers.ModelSerializer):
    followers = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = '__all__'

    def get_followers(self, obj):
        followers_usernames = obj.followers.values_list('username', flat=True)
        return followers_usernames



class UserProfileSerializer(serializers.ModelSerializer):
    like_movies = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('id', 'username', 'nickname', 'introduce', 'profileimg', 'like_movies')
        read_only_fields = ('username',)

    def get_like_movies(self, obj):
        liked_movie_ids = obj.like_movies.values_list('id', flat=True)
        return liked_movie_ids


