from django.contrib import admin
from .models import CustomUser, Blog, Comment

admin.site.register(CustomUser)
admin.site.register(Blog)
admin.site.register(Comment)