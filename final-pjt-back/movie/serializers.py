from rest_framework import serializers
from .models import Movie, Review, Keyword, Genre

class ReviewSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ('movie', 'user',)


class MovieDetailSerializer(serializers.ModelSerializer):
    review_set = ReviewSerializer(many=True, read_only=True)
    like_users = serializers.IntegerField(source='like_users.count', read_only=True)
    class Meta:
        model = Movie
        fields = '__all__'

class MovieDataBaseSerializer(serializers.ModelSerializer):
    review_set = ReviewSerializer(many=True, read_only=True)
    like_users = serializers.IntegerField(source='like_users.count', read_only=True)
    class Meta:
        model = Movie
        fields = '__all__'

class MovieLikeSerializer(serializers.ModelSerializer):
    like_users = serializers.IntegerField(source='like_users.count', read_only=True)
    class Meta:
        model = Movie
        fields = ('like_users',)
        # read_only_fields = ('user','title','content', )
        
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