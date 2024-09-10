from django.contrib import admin
from .models import Review

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ["title", "published_at", "author", "rating"]
    list_filter = ["author", "status","rating"]