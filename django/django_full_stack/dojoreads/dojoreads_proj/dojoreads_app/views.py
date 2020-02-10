from django.shortcuts import render, redirect, HttpResponse
from login_n_registration_app.models import User
from .models import *
# Create your views here.


def books(request, user_id):
    context = {
        'user': User.objects.all().get(id=user_id),
        'reviews': Review.objects.all().order_by("-created_at"),
        'books': Book.objects.all(),
    }

    return render(request, 'books.html', context)


def logout(request):
    request.session['user_id'] = None
    return redirect("/")


def add_book_and_review(request, user_id):
    context = {
        'user': User.objects.all().get(id=user_id),
        'books': Book.objects.all()
    }

    return render(request, 'add_book.html', context)


def book_preview(request, user_id, book_id):
    context = {
        'user': User.objects.all().get(id=user_id),
        'book': Book.objects.all().get(id=book_id)
    }

    return render(request, 'book_preview.html', context)


def user_review(request, user_id):
    user = User.objects.all().get(id=user_id)

    context = {
        'user': user,
        'books': Book.objects.all().filter(user=user),
        'reviews': Review.objects.all().filter(user=user),
    }

    return render(request, 'user_review.html', context)


def handle_adding(request, user_id):
    user = User.objects.all().get(id=user_id)
    book_title = request.POST['book_title']

    author = ""
    if 'new_author' in request.POST:
        author = request.POST['new_author']
    elif 'author' in request.POST:
        author = request.POST['author']

    review = request.POST['review']
    ratings = request.POST['inlineRadioOptions']

    new_book = Book.objects.create(title=book_title, author=author, user=user)
    new_review = Review.objects.create(
        text=review, rating=ratings, book=new_book, user=user)
    return redirect(f"/books/{user_id}")


def add_review(request, user_id):
    book = Book.objects.all().get(id=request.POST['book_id'])
    user = User.objects.all().get(id=user_id)

    new_review = Review.objects.create(
        text=request.POST['review'], rating=request.POST['inlineRadioOptions'], book=book, user=user)
    book.reviews.add(new_review)

    context = {
        'user': user, 'book': book
    }

    return redirect(f"/books/{user.id}/{book.id}")


def remove_review(request, user_id, review_id):
    review = Review.objects.all().get(id=review_id)
    review.delete()
    return redirect(f"/books/{user_id}/{review.book.id}")
