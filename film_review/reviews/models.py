from django.db import models
from django.contrib.auth.models import User

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
    status = models.IntegerField(choices=Status.choices, default=Status.DRAFT)
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=Rating.choices, default=Rating.BAD)
    

"""
model reviews

id: A primary key integer field that uniquely identifies each review.
title: A string field to store the title of the review limited to 200 characters.
status: An integer field to store the status of the review (Draft or Published).
body: A text field to store the main content of the review.
author_id: An integer field to create a relationship between the review and the user who authored it, referencing the User table's primary key.
rating: An integer field to store the rating of the review (BAD, POOR, FAIR, GOOD, EXCELLENT, EXCEPTIONAL).
published_at: A datetime field to store when the review was published.
created_at: A datetime field to store when the review record was created.
updated_at: A datetime field to store when the review record was lats updated.
"""