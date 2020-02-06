from django.shortcuts import render, redirect, HttpResponse

# Create your views here.

users = []


def index(request):
    context = {
        'name': 'ewrewr',
        'hobbies': ['wetrwet', 'wtwtwet', 'wetwtewt'],
        'users': users
    }

    return render(request, 'index.html', context)


def new(request):
    users.append(request.POST['email'])
    return redirect("/")
