from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from ..models import CustomUser
from ..serializers import CustomUserSerializer


@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
    token_serializer = TokenObtainPairSerializer(data = request.data)
    if token_serializer.is_valid():
        tokens = token_serializer.validated_data
        user = get_object_or_404(CustomUser, username = request.data.get('username'))
        response_data = {
            "access_token": tokens['access'],
            "refresh_token": tokens['refresh'],
            "user": {
                'username': user.username,
                'email': user.email,
            }
        }
        return Response(response_data, status=status.HTTP_200_OK)
    return Response(token_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    serializer = CustomUserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)