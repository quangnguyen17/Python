from django.shortcuts import render, redirect, HttpResponse
from .models import *


def home(request):
    context = {'books': Book.objects.all()}
    return render(request, 'index.html', context)


def authors(request):
    authors = Author.objects.all()
    context = {'authors': authors}
    return render(request, 'authors.html', context)


def author(request, id):
    context = {
        'author': Author.objects.all().get(id=id),
        'books': Book.objects.all(),
        'author_books': Author.objects.all().get(id=id).books.all()
    }
    return render(request, 'author.html', context)


def add_book(request):
    Book.objects.create(title=request.POST['title'], desc=request.POST['desc'])
    return redirect("/")


def remove_book(request, id):
    Book.objects.all().get(id=id).delete()
    return redirect("/")


def add_author(request):
    Author.objects.create(
        first_name=request.POST['first_name'], last_name=request.POST['last_name'], notes=request.POST['notes'])
    return redirect("/authors")


def remove_author(request, id):
    Author.objects.all().get(id=id).delete()
    return redirect("/authors")


def book(request, id):
    book = Book.objects.all().get(id=id)
    book_authors = book.authors.all()

    for author in book_authors:
        print(author.first_name)

    context = {
        'book': book,
        'book_authors': book_authors,
        'authors': Author.objects.all()
    }

    return render(request, 'book.html', context)


def add_author_to_book(request, book_id):
    author_id = request.POST['id']
    author = Author.objects.all().get(id=author_id)

    book = Book.objects.all().get(id=book_id)
    book.authors.add(author)
    return redirect(f"/book/{book_id}")


def remove_author_from_book(request, book_id):
    return redirect(f"/book/{book_id}")


def add_book_to_author(request, author_id):
    book = Book.objects.all().get(id=request.POST['book_id'])
    Author.objects.all().get(id=author_id).books.add(book)
    return redirect(f"/author/{author_id}")
