from rest_framework import serializers
from .models import Movie, Review


class ReviewSerializer(serializers.ModelSerializer):
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
        
class MovieLikeSerializer(serializers.ModelSerializer):
    like_users = serializers.IntegerField(source='like_users.count', read_only=True)
    class Meta:
        model = Movie
        fields = ('like_users',)
        read_only_fields = ('user','title','content', )