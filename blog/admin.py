from django.contrib import admin
from .models import Post, Comment, Like, Profile  # Import the Profile model

# Register the Profile model
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(Profile)
