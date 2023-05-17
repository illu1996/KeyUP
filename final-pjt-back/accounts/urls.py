from django.urls import path
from . import views


urlpatterns = [
    path('follow/', views.follow, name='follow'),
    path('updateprofile/', views.updateprofile, name='updateprofile'),
]
