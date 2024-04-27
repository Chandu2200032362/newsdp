from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Review
from .forms import ReviewForm


# Create your views here.

def review_list(request):
    if request.method == 'GET':
        review = Review.objects.all()
        return render(request, 'feedback.html', {'reviews': review})


def add_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.save()
            return redirect('review_list')
        else:
            form = ReviewForm()
        return render(request, 'feedback.html', {'form': form})