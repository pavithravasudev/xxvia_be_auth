from django.shortcuts import render
from xxvia_be_auth_app.models import User
from xxvia_be_auth_app.serializers import UserSerializer
from rest_framework import generics

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view

#List and Detail View implemented for User Model

@api_view(['POST'])
def user_list(request):
    if request.method == 'POST':
        user_data = JSONParser().parse(request)
        user_serializer = UserSerializer(data=user_data)
        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse(user_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(user_serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def user_detail(request, id):
    try:
        user_data = User.objects.get(id=id)
    except User.DoesNotExist:
        return JsonResponse({'message': 'The User does not exist'}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        user_serializer = UserSerializer(user_data)
        return JsonResponse(user_serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        user_serializer = UserSerializer(user_data, data=request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse(user_serializer.data, status=status.HTTP_200_OK)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'PATCH':
        user_serializer = UserSerializer(user_data, data=request.data, partial=True)
        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse(user_serializer.data, status=status.HTTP_200_OK)
        return JsonResponse(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        User.delete(user_data)
        return JsonResponse({'message': 'The User is deleted successfully.'}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def user_validation(request, username):
    try:
        user_data = User.objects.get(username=username)
    except User.DoesNotExist:
        return JsonResponse({'message': 'The User does not exist'}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        user_serializer = UserSerializer(user_data)
        return JsonResponse(user_serializer.data, status=status.HTTP_200_OK)