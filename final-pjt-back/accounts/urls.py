from django.urls import path
from . import views


urlpatterns = [
    path('<int:user_pk>/follow/', views.follow, name='follow'),
    path('<int:user_pk>/updateprofile/', views.updateprofile, name='updateprofile'),
    path('<str:username>/profile/', views.profile, name='profile'),
]
