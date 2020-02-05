from django.shortcuts import render, HttpResponse, redirect
import random
from datetime import datetime

# Create your views here.


def randomAmount(str):
    amount = 0

    if str == "farm":
        amount = random.randint(10, 21)
    elif str == "cave":
        amount = random.randint(5, 10)
    elif str == "house":
        amount = random.randint(2, 5)
    elif str == "casino":
        amount = random.randint(0, 50) if random.randint(
            0, 2) == 1 else random.randint(-50, 0)

    return amount


def index(request):
    if 'amounts' not in request.session:
        request.session['amounts'] = []

    if 'gold' not in request.session:
        request.session['gold'] = 0

    if 'now' not in request.session:
        request.session['now'] = ""

    return render(request, 'index.html')


def process_money(request, place):
    amount = randomAmount(place)
    now = datetime.now().strftime("%d/%m/%Y %H:%M:%S %p")
    verb = "Earned" if amount > 0 else "Lost"
    request.session['amounts'].append(
        {'amount': amount, 'place': place, 'verb': verb})
    request.session.save()
    request.session['gold'] += amount
    request.session['now'] = now
    return redirect("/")


def process_money_with_golds(request, place, golds):
    amount = randomAmount(place)
    now = datetime.now().strftime("%d/%m/%Y %H:%M:%S %p")
    verb = "Earned" if amount > 0 else "Lost"
    request.session['amounts'].append(
        {'amount': amount, 'place': place, 'verb': verb})
    request.session.save()
    request.session['gold'] += amount
    request.session['now'] = now
    return redirect("/")
