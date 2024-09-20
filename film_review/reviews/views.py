from django.shortcuts import render

from reviews.models import Review

def review_list(request):
    reviews = Review.published.all()
    return render(request, "reviews/list.html", {"reviews": reviews})

def review_datail(request, id):
    review = Review.published.get(id=id)
    return render(request, "reviews/detail.html", {"review": review})