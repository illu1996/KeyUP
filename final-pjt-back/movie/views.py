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

from random import sample
# Create your views here.

@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def movie_list(request):
    if request.method == 'GET':
        # articles = Article.objects.all()
        movies = get_list_or_404(Movie)
        movies = sample(movies, 15)
        serializer = MovieListSerializer(movies, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    if request.method == 'GET':
        serializer = MovieDetailSerializer(movie)
        return Response(serializer.data)

@api_view(['POST'])   
def movie_create(request):
    serializer = MovieListSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


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
        
@api_view(['GET', 'POST'])
def review_create(request, movie_pk):
    # article = Article.objects.get(pk=article_pk)
    movie = get_object_or_404(Movie, pk=movie_pk)
    if request.method=='GET':
        reviews = Review.objects.filter(movie=movie)
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)

    if request.method=='POST':
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(movie=movie, user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['POST'])
def like(request, movie_pk):
    if request.user.is_authenticated:

        movies = Movie.objects.all()
        # movieIdList = [movie['movie_id'] for movie in movies ]
        # print(movieIdList)
        for movie in movies:
            if movie.movie_id == movie_pk:
                break
            else:
                continue
        else:
            serializer = MovieDetailSerializer(data=request.data)

            if serializer.is_valid(raise_exception=True):

                serializer.save()
        movie = get_object_or_404(Movie, movie_id=movie_pk)
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
    movies = get_list_or_404(Movie, movie_keyword=keyword_pk)
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def search_movies_list(request, keyword_str):
    movies = Movie.objects.all()
    movies = Movie.objects.filter(title__icontains=keyword_str)
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)