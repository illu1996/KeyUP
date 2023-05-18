from rest_framework.response import Response
from rest_framework.decorators import api_view
# Authentication Decorators
from rest_framework.decorators import authentication_classes

# permission Decorators
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

from rest_framework import status
from django.shortcuts import get_object_or_404, get_list_or_404
from .models import Movie, Review, Keyword, Genre
from .serializers import MovieDetailSerializer, ReviewSerializer,\
    MovieLikeSerializer, MovieListSerializer, KeywordListSerializer,\
    KeywordMovieSerializer, GenreSerializer
# Create your views here.

@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def movie_list(request):
    if request.method == 'GET':
        # articles = Article.objects.all()
        movies = get_list_or_404(Movie)
        serializer = MovieListSerializer(movies, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    if request.method == 'GET':
        serializer = MovieDetailSerializer(movie)
        return Response(serializer.data)

@api_view(['GET'])
def genre_list(request):
    genres = get_list_or_404(Genre)
    serializer = GenreSerializer(genres, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def review_list(request):
    if request.method == 'GET':
        # comments = Comment.objects.all()
        reviews = get_list_or_404(Review)
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)
    
@api_view(['GET', 'DELETE', 'PUT'])
def review_detail(request, review_pk):
    # review = review.objects.get(pk=review_pk)
    review = get_object_or_404(Review, pk=review_pk)

    if request.method == 'GET':
        serializer = ReviewSerializer(review)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        if request.user == review.user :
            review.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

    elif request.method == 'PUT':
        if request.user == review.user :
            serializer = ReviewSerializer(review, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        
@api_view(['POST'])
def review_create(request, movie_pk):
    # article = Article.objects.get(pk=article_pk)
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = ReviewSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(movie=movie, user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['POST'])
def like(request, movie_pk):
    if request.user.is_authenticated:
        movie = get_object_or_404(Movie, pk=movie_pk)
        user = request.user
        if movie.like_users.filter(pk=user.pk).exists():
            movie.like_users.remove(user)
        else:
            movie.like_users.add(user)
        serializer = MovieLikeSerializer(movie, data=request.data)
        if serializer.is_valid(raise_exception=True):
            return Response(serializer.data, status=status.HTTP_200_OK)

    return Response(status=status.HTTP_401_UNAUTHORIZED)

    
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def keyword_list(request):
    if request.method == 'GET':
        keywords = get_list_or_404(Keyword)
        serializer = KeywordListSerializer(keywords, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def keyword_detail_movies(request, keyword_pk):
    keyword = get_object_or_404(Keyword, pk=keyword_pk)
    movies = get_list_or_404(Movie, movie_keyword=keyword_pk)
    serializer = KeywordMovieSerializer(movies, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

    # if request.method == 'GET':
    #     keywords = get_list_or_404(keyword)
    #     serializer = KeywordListSerializer(keywords, many=True)
    #     return Response(serializer.data, status=status.HTTP_200_OK)
    
     