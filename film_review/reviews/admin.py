from django.contrib import admin
from .models import Review

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ["title", "slugified_title", "published_at", "author", "rating"]
    list_filter = ["author", "status","rating"]
    search_fields = ["title", "author__username"]
    prepopulated_fields = {"slugified_title": ["title"]}