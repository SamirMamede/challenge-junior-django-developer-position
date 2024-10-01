from django.contrib import admin
from .models import Review, Comment

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ["title", "slugified_title", "published_at", "author", "rating"]
    list_filter = ["author", "status", "rating"]
    search_fields = ["title", "author__username"]
    prepopulated_fields = {"slugified_title": ["title"]}

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ["review", "user_name", "user_email", "message", "active"]
    list_filter = ["created_at", "active"]
    search_fields = ["user_name", "user_email", "message"]