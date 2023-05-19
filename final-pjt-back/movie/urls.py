from django.urls import path
from . import views

urlpatterns = [
    path('', views.movie_list),
    path('<int:movie_pk>/', views.movie_detail),
    path('create/', views.movie_create),
    path('reviews/', views.review_list),
    path('reviews/<int:review_pk>/', views.review_detail),
    path('<int:movie_pk>/reviews/', views.review_create),
    path('<int:movie_pk>/like/', views.like),
    path('keywords/', views.keyword_list),
    path('keywords/<int:keyword_pk>/', views.keyword_detail_movies),
    path('genres/', views.genre_list)

]
