from django.contrib import admin
from django.contrib.admin import register

from .models import Comment, Post


@register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "created_at", "updated_at")
    list_filter = ("author", "created_at", "updated_at")
    search_fields = ("title", "body")
    list_per_page = 10


@register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("post", "author", "created_at", "updated_at")
    list_filter = ("post", "author", "created_at", "updated_at")
    search_fields = ("post", "body")
    list_per_page = 10
