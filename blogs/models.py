from django.contrib.auth.models import AbstractUser, User
from django.db import models


class CustomUser(AbstractUser):
    birthdate = models.DateField(null=True, blank=True)
    profile_image = models.ImageField(null=True, blank=True, upload_to='profile_images/')


class Blog(models.Model):
    CATEGORY_CHOICES = [
        ('Technology', 'Technology'),
        ('Science', 'Science'),
        ('Travel', 'Travel'),
    ]
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='blogs_authored')
    title = models.CharField(max_length=255)
    content = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    feature_image = models.ImageField(upload_to='blog_images/', null=True, blank=True)
    upvote_count = models.IntegerField(default=0)
    like_count = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class Comment(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='comments')
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='blog_comments')
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user