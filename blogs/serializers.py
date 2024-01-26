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


class BlogSerializer(serializers.ModelSerializer):
    feature_image = serializers.ImageField(allow_null=True)

    class Meta:
        model = Blog
        fields = ['title', 'content', 'category', 'feature_image', 'author', 'upvote_count', 'like_count']


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
