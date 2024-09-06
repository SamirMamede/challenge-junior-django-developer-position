from django.db import models

"""
model reviews

id: A primary key integer field that uniquely identifies each review.
title: A string field to store the title of the review (Draft or Published).
status: An integer field to store the main content of the review.
body: A text field to store the main content of the review.
author_id: An integer field to create a relationship between the review and the user who authored it, referencing the User table's primary key.
rating: An integer field to store the rating of the review (BAD, POOR, FAIR, GOOD, EXCELLENT, EXCEPTIONAL).
published_at: A datetime field to store when the review was published.
created_at: A datetime field to store when the review record was created.
updated_at: A datetime field to store when the review record was lats updated.
"""