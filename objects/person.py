#!/usr/bin/env python3
from enum import Enum


class Gender(Enum):
    FEMALE = 1
    MALE = 2
    NONE = 3


class SexualOrientation(Enum):
    HOMOSEXUAL = 1
    HETEROSEXUAL = 2
    ASEXUAL = 3


class Race(Enum):
    HUMAN = 1
    DWARF = 2
    NIXE = 3
    ELF = 4


class Language(Enum):
    DEF = 1


class Profession(Enum):
    Alchemist = 0
    Arbeitsloser_Tunichtsgut = 1
    Architekt = 2
    Arzt = 3
    Bauearbeiter = 4
    Bauer = 5
    Bierbrauer = 6
    Bogenmacher = 7
    Bootsbauer = 8
    Bote = 9
    Braumeister = 10
    Buchhändler = 11
    Bäcker = 12
    Dockarbeiter = 13
    Fischer = 14
    Färber = 15
    Geistlicher = 16
    Gelehrter = 17
    Gerber = 18
    Goldschmied = 19
    Hebamme = 20
    Hirte = 21
    Hof_Gärtner = 22
    Hofnarr = 23
    Holzfäller = 24
    Hufschmied = 25
    Händler = 26
    Imker = 27
    Jäger = 28
    Kapitän = 29
    Koch = 30
    Krämer = 31
    Käsner = 32
    Lehrer = 33
    Metzger = 34
    Musikant = 35
    Müller = 36
    Prostituierte = 37
    Schankwirt = 38
    Schauspieler = 39
    Schmied = 40
    Schneider = 41
    Schreiner = 42
    Schuster = 43
    Seemann = 44
    Soldat = 45
    Stadtwache = 46
    Stallbursche = 47
    Steinmetz = 48
    Totengräber = 49
    Töpfer = 50
    Zimmermädchen = 51


class Person(object):
    def __init__(self):
        super(Person, self).__init__()
        self.__name = 'John Doe'
        self.__gender = "f"
        self.__address = ""
        self.__race = ""
        self.__height = ""
        self.__languages = ""

        self.__profession = ""

        self.__father = ""
        self.__mother = ""
        self.__children = ""
        self.__pets = ""

        self.__relations = ""

        self.__notes = ""

        self.__stats = ""
        self.__sexual_orientation = ""

        self.__inventroy = ""

    @property
    def name(self):
        return self.__name

    @property
    def gender(self):
        return self.__gender

    @property
    def address(self):
        return self.__address

    @property
    def race(self):
        return self.__race

    @property
    def height(self):
        return self.__height

    @property
    def profession(self):
        return self.__profession

    @property
    def father(self):
        return self.__father

    @property
    def mother(self):
        return self.__mother

    @property
    def children(self):
        return self.__children

    @property
    def pets(self):
        return self.__pets

    @property
    def relations(self):
        return self.__relations

    @property
    def notes(self):
        return self.__notes

    @property
    def stats(self):
        return self.__stats

    @property
    def sexual_orientation(self):
        return self.__sexual_orientation

    @property
    def languages(self):
        return self.__languages

    @property
    def inventroy(self):
        return self.__inventroy
