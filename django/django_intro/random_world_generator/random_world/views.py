from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string
# Create your views here.


def index(request):
    request.session['counter'] = 0
    return HttpResponse("random_world.")


def random_world(request):
    request.session['counter'] += 1
    ran_wd = get_random_string(length=14)
    context = {'random_world': ran_wd}
    return render(request, 'random_world.html', context)


def reset(request):
    request.session['counter'] = 0
    return redirect('/random_world')
