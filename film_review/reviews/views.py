from django.shortcuts import get_object_or_404, render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpRequest
from django.views.decorators.http import require_POST
from django.contrib import messages
from reviews.models import Review, Comment
from .forms import CommentForm

def review_list(request):
    reviews = Review.published.all()
    paginator = Paginator(reviews, 4)
    page_number = request.GET.get("page", 1)

    try:
        reviews_page = paginator.page(page_number)
    except (EmptyPage, PageNotAnInteger):
        reviews_page = paginator.page(1)

    return render(request, "reviews/list.html", {"reviews_page": reviews_page})

def review_datail(request, year, month, day, slugified_title):
    form = CommentForm()
    review = get_object_or_404(
        Review.published, 
        published_at__year=year, 
        published_at__month=month, 
        published_at__day=day, 
        slugified_title=slugified_title
    )
    
    return render(request, "reviews/detail.html", {"review": review, "form": form})

@require_POST
def add_comment(request, review_id):
    review: Review = get_object_or_404(Review.published, id=review_id)
    form = CommentForm(data=request.POST)

    if form.is_valid():
        comment: Comment = form.save(commit=False)
        comment.review = review
        comment.save()
        messages.success(request, "Your comment was added successfully!")
        return redirect(review)
    else:
        return render(request, "reviews/detail.html", {"review": review, "form": form})