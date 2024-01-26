from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from ..models import Blog, CustomUser
from ..serializers import BlogSerializer
import copy


@api_view(['GET'])
@permission_classes([AllowAny])
def blog_list(request):
    blogs = Blog.objects.all()
    serializer = BlogSerializer(blogs, many=True)
    blogs_list = serializer.data
    print(blogs_list)
    return Response(blogs_list, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_blog(request):
    data = copy.deepcopy(request.data)
    username = data.get('author')
    author_id = get_object_or_404(CustomUser, username=username).id
    data['author'] = author_id
    serializer = BlogSerializer(data = data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST','DELETE'])
def manage_blog(request):
    pass
