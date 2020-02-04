from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, HttpResponse


def index(request):
    return HttpResponse("this is the equivalent of @app.route('/')!")


def first_statement(request):
    # return HttpResponse("Hello, World!")
    return HttpResponse("First Statement")


def second_statement(request):
    return HttpResponse("Second Statement")
