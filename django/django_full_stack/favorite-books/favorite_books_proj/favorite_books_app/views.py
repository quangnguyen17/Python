from django.shortcuts import render, redirect, HttpResponse
from login_n_registration_app.models import *
from .models import *
from login_n_registration_app.models import *
# Create your views here.


def index(request, user_id):
    if 'user_id' in request.session:
        if request.session['user_id'] != None:
            context = {
                'user': User.objects.all().get(id=user_id),
                'books': Book.objects.all()
            }
            return render(request, 'books.html', context)
        else:
            return redirect("/")
    else:
        return redirect("/")


def log_out(request):
    request.session['user_id'] = None
    return redirect("/")


def book_preview(request, user_id, book_id):
    context = {
        'user': User.objects.all().get(id=user_id),
        'book': Book.objects.all().get(id=book_id)
    }

    return render(request, 'book.html', context)


def upload_book(request, user_id):
    user = User.objects.all().get(id=user_id)
    book = Book.objects.create(
        title=request.POST['title'], desc=request.POST['desc'], uploaded_by=user)
    book.users.add(user)
    return redirect("/")


def favorite(request, user_id, book_id):
    Book.objects.all().get(id=book_id).users.add(User.objects.all().get(id=user_id))
    return redirect(f"/books/{user_id}")


def favorite_2(request):
    Book.objects.all().get(id=request.POST['book_id']).users.add(
        User.objects.all().get(id=request.POST['user_id']))
    return redirect(f"/books/preview/{request.POST['user_id']}/{request.POST['book_id']}")


def update(request, user_id):
    book = Book.objects.all().get(id=request.POST['book_id'])

    if 'update' in request.POST:
        book.desc = request.POST['desc']
        book.save()

    if 'delete' in request.POST:
        book.delete()
        book.save()
        return redirect(f"/books/{user_id}")

    return redirect(f"/books/preview/{user_id}/{request.POST['book_id']}")
