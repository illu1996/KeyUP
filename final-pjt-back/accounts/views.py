from django.shortcuts import render, redirect, get_object_or_404
from rest_framework.decorators import api_view
from django.contrib.auth import get_user_model
from .serializers import UserSerializer, UserProfileSerializer
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
@api_view(['GET', 'POST'])
def follow(request, user_pk):
    if request.method =='GET':
        person = get_object_or_404(get_user_model(), pk=user_pk)
        serializer = UserSerializer(person)
        response_data = {
            'followers_count': person.followers.count(),
            'followings_count': person.followings.count(),
            'person': serializer.data
        }
        return Response(response_data)


    if request.method =='POST':
        if request.user.is_authenticated:
            person = get_object_or_404(get_user_model(), pk=user_pk)
            user = request.user
            if person != user:
                if person.followers.filter(pk=user.pk).exists():
                    person.followers.remove(user)
                    is_followed = False
                else:
                    person.followers.add(user)
                    is_followed = True
                serializer = UserSerializer(person)
                response_data = {
                    'is_followed': is_followed,
                    'followers_count': person.followers.count(),
                    'followings_count': person.followings.count(),
                    'person': serializer.data
                }
                return Response(response_data)
        return Response(status=status.HTTP_401_UNAUTHORIZED)   

@api_view(['GET'])
def profile(request, username):
    
    user = get_object_or_404(get_user_model(), username=username)
    serializer = UserProfileSerializer(user)
    print(serializer.data)
    return Response(serializer.data)



@api_view(['POST', 'GET'])
def updateprofile(request, user_pk):
    user = get_object_or_404(get_user_model(), pk=user_pk)
    if request.method =='GET':
        serializer = UserProfileSerializer(user)
        return Response(serializer.data)
    if request.method=='POST':
        if request.user.is_authenticated:
            person = get_object_or_404(get_user_model(), pk=user_pk)
            user = request.user
            if person == user:
                serializer = UserProfileSerializer(person, data=request.data)
                if serializer.is_valid(raise_exception=True):
                    serializer.save()
                    return Response(serializer.data)
    return Response(status=status.HTTP_401_UNAUTHORIZED) 
            
