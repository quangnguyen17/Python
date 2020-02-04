
from django.shortcuts import render, HttpResponse, redirect

# Create your views here.


def index(request):
    # return HttpResponse("placeholder to later display a list of all blogs")
    return render(request, "index.html")


def new(request):
    return HttpResponse("placeholder to display a new form to create a new blog")


def hello(request, name):
    context = {
        "name": name
    }

    return render(request, "hello.html", context)


def create(request):
    return redirect("/")


def show(request, number):
    return HttpResponse(f"placeholder to display blog number: {number}")


def edit(request, number):
    return HttpResponse(f"placeholder to edit blog {number}")


def destroy(request, number):
    return redirect("/")


def delete(request, id):
    return redirect(f"/{id}")
