from django.shortcuts import render
from django.http import HttpResponse

from my_system import System
import os

from objects.person import get_random_person

# Create your views here.


def index(request):
    charakter = get_random_person()

    context = {
        "charakter": charakter,
        "dm": True
    }
    return render(request, 'charactersheet/charactersheet.html', context)
