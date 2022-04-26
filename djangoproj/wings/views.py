from django.shortcuts import render
from django.http import HttpResponse
from django.utils.translation import gettext_lazy as _


def testlang(request):
    return HttpResponse(_('Welcome to language translation!'))

def index(request):
    return render(request, "index.html")

def openPrice(request):
    return render(request, "openPrice.html")

def menu(request):
    return render(request, "menu.html")

def booking(request):
    return render(request, "booking.html")
