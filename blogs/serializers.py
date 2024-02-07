# yourappname/serializers.py
from rest_framework import serializers
from django.db import models
from .models import CustomUser, Blog, Comment


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'password', 'username', 'email', 'birthdate')

    def create(self, validated_data):
        user = CustomUser(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user


class UserProfileSerializer(serializers.ModelSerializer):
    profile_image = serializers.ImageField(use_url=True, required=False, allow_null=True)

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'birthdate', 'profile_image')
        extra_kwargs = {'password': {'write_only': True, 'required': False}}


class BlogSerializer(serializers.ModelSerializer):
    cover_image = serializers.ImageField(allow_null=True, required=False)

    class Meta:
        model = Blog
        fields = ['title', 'content', 'category', 'cover_image', 'author', 'upvote_count', 'like_count','pk']


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
