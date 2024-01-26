from django.contrib import admin
from django.urls import path,include
from .views import user_view, blog_views

urlpatterns = [
    # USER
    path('login', user_view.login, name='user-login'),
    path('register', user_view.register, name='user-register'),

    # BLOGS
    path('', blog_views.blog_list, name='blog-list'),
    path('create_blog', blog_views.create_blog, name='create-blog')

]
