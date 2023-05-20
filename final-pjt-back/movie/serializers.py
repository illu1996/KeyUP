from rest_framework import serializers
from .models import Movie, Review, Keyword, Genre

class ReviewSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ('movie', 'user',)


class MovieDetailSerializer(serializers.ModelSerializer):
    like_users = serializers.SerializerMethodField(read_only=True)
    review_set = ReviewSerializer(many=True, read_only=True)
    like_users_cnt = serializers.IntegerField(source='like_users.count', read_only=True)
    class Meta:
        model = Movie
        fields = '__all__'
    def get_like_users(self, obj):
        liked_users_username = obj.like_users.values_list('username', flat=True)
        return liked_users_username

class MovieDataBaseSerializer(serializers.ModelSerializer):
    review_set = ReviewSerializer(many=True, read_only=True)
    like_users = serializers.IntegerField(source='like_users.count', read_only=True)
    class Meta:
        model = Movie
        fields = '__all__'

class MovieLikeSerializer(serializers.ModelSerializer):
    like_users = serializers.SerializerMethodField()
    like_users_cnt = serializers.IntegerField(source='like_users.count', read_only=True)
    class Meta:
        model = Movie
        fields = ('like_users', 'like_users_cnt',)
        # read_only_fields = ('user','title','content', )
    def get_like_users(self, obj):
        liked_users_username = obj.like_users.values_list('username', flat=True)
        return liked_users_username
        
class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = "__all__"
        
class KeywordListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Keyword
        fields = "__all__"
        read_only_fields =('movie_id',)

class KeywordMovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('movie_id',)

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'