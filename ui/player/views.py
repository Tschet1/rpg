from django.shortcuts import render
from django.http import HttpResponse

from my_system import System
import os

from objects.person import get_random_person, load_person_with_name

# Create your views here.


def index(request):
    charakter = get_random_person()

    context = {
        "charakter": charakter,
        "dm": True
    }

    charakter.sheet.Stärke.value = 5
    charakter.sheet.Stärke.add_malus(15, "Klein")
    charakter.sheet.Stärke.add_bonus(5, "Bürger aus Altheim")

    charakter.sheet.Reiten.value = 5
    charakter.sheet.Reiten.add_malus(15, "Klein")
    charakter.sheet.Reiten.add_bonus(5, "Bürger aus Altheim")
    return render(request, 'charactersheet/charactersheet.html', context)

def get_person(request, name):
    print("Looking for " + name)
    person = load_person_with_name(name)

    context = {
        "charakter": person,
        "id": person.name,
        "dm": True
    }

    return render(request, 'charactersheet/charactersheet.html', context)
