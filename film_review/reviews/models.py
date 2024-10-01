from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User

class PublishedManager(models.Manager):
    def get_queryset(self) -> models.QuerySet:
        return super().get_queryset().filter(status=Review.Status.PUBLISHED)

class Review(models.Model):
    class Status(models.IntegerChoices):
        DRAFT = (1, "Draft")
        PUBLISHED = (2, "Published")

    class Rating(models.IntegerChoices):
        BAD = (1, "Bad")
        POOR = (2, "Poor")
        FAIR = (3, "Fair")
        GOOD = (4, "Good")
        EXCELLENT = (5, "Excellent")
        EXCEPTIONAL = (6, "Exceptional")

    title = models.CharField(max_length=200)
    slugified_title = models.SlugField(max_length=200, unique_for_date="published_at")
    status = models.IntegerField(choices=Status.choices, default=Status.DRAFT)
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=Rating.choices, default=Rating.GOOD)
    published_at = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = models.Manager()
    published = PublishedManager()

    def get_absolute_url(self):
        from django.urls import reverse

        return reverse(
            "reviews:review_detail", 
            args=[self.published_at.year, self.published_at.month, self.published_at.day, self.slugified_title],
        )

    def __str__(self) -> str:
        return self.title

class Comment(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=200)
    user_email = models.EmailField()
    message = models.TextField()
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)