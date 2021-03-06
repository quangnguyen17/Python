from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import *
# Create your views here.


def index(request):
    return redirect('/shows')


def shows(request):
    return render(request, 'index.html', {'shows': Show.objects.all()})


def new(request):
    return render(request, 'new.html')


def shows_id(request, id):
    return render(request, 'read.html', {'show': Show.objects.all().get(id=id)})


def shows_edit(request, id):
    return render(request, 'update.html', {'show': Show.objects.all().get(id=id)})


# CRUD Functions
def add_show(request):
    errors = Show.objects.creation_validator(request.POST)

    if len(errors) > 0:
        for key, val in errors.items():
            messages.warning(request, val)

        return render(request, "new.html")
    else:
        title = request.POST['title']
        network = request.POST['network']
        release_date = request.POST['release_date']
        desc = request.POST['desc']
        Show.objects.create(title=title, network=network,
                            release_date=release_date, desc=desc)

        return redirect("/shows")


def delete_show(request, id):
    Show.objects.all().get(id=id).delete()
    return redirect("/shows")


def save_edit(request, id):
    errors = Show.objects.creation_validator(request.POST)

    if len(errors) > 0:
        for key, val in errors.items():
            messages.warning(request, val)

        return redirect(f"shows/{id}/save")
    else:
        title = request.POST['title']
        network = request.POST['network']
        release_date = request.POST['release_date']
        desc = request.POST['desc']

        show = Show.objects.all().get(id=id)
        show.title = title
        show.network = network
        show.release_date = release_date
        show.desc = desc
        show.save()
        return redirect("/")
