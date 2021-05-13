#!/usr/bin/env python3
from __future__ import annotations
from enum import Enum
from .address import Address
from my_system import create_charactersheet
from .relation import Opinion, Relation
from .item import Item


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

    Animal = 52


class Person(object):
    def __init__(self,
                 name: str,
                 age: int,
                 gender: Gender,
                 address: Address,
                 race: Race,
                 height: int,
                 languages: list,
                 profession: Profession,
                 sexorient: SexualOrientation):

        super(Person, self).__init__()
        self.__name = name
        self.__gender = gender
        self.__address = address
        self.__race = race
        self.__height = height
        self.__languages = languages

        self.__profession = profession

        self.__father = None
        self.__mother = None
        self.__children = None
        self.__pets = None

        self.__relations = []

        self.__notes = []

        self.__sheet = create_charactersheet()
        self.__sexual_orientation = sexorient

        self.__inventroy = {}

        # TODO: create getter/setters
        self.__age = age
        self.__is_alive = True

        # TODO:
        #hp/mana usw.
        #attack, defense, weight of inventory

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

    @father.setter
    def father(self, father: Person):
        self.__father = father

    @property
    def mother(self):
        return self.__mother

    @mother.setter
    def mother(self, mother: Person):
        self.__mother = mother

    @property
    def children(self):
        return self.__children

    def add_child(self, child: Person):
        self.__children.append(child)

    @property
    def pets(self):
        return self.__pets

    def add_pet(self, animal: Person):
        self.__children.append(animal)

    def get_opinion(self, towards: Person):
        opinion = [(opinion.effect, opinion.reason)
                   for opinion in self.__relations if opinion.towards == towards
                   ]
        return (sum([op[0] for op in opinion]), opinion)

    def get_family_opinion(self, towards: Person, relative_weight=0.5):
        _, relations = self.get_opinion()

        def _get_opinion(person: Person, towards: Person, rel_status: str, relations: list, relative_weight):
            if person is not None:
                _, t_relations = person.get_opinion(towards)
                relations.extend([
                    (effect * relative_weight, f"{person.name} ({rel_status}): {reason}") for effect, reason in t_relations
                ])
            return relations

        relations = _get_opinion(self.father, towards,
                                 "Vater", relations, relative_weight)
        relations = _get_opinion(self.mother, towards,
                                 "Mutter", relations, relative_weight)
        for child in self.children:
            relations = _get_opinion(
                child, towards, "Kind", relations, relative_weight)

        # TODO: reflect what happens if someone doesn't like his/her parents or children
        return (sum([op[0] for op in relations]), relations)

    def add_opinion(self, towards: Person, effect: Opinion, reason: str):
        self.__relations.append(Relation(towards, reason, effect))

    @property
    def notes(self):
        return self.__notes

    def add_note(self, note: str):
        self.__notes.append(note)

    @property
    def sexual_orientation(self):
        return self.__sexual_orientation

    @property
    def languages(self):
        return self.__languages

    def add_language(self, language: Language):
        self.__notes.append(language)

    @property
    def inventroy(self):
        # TODO: maybe format this
        return self.__inventroy

    def add_to_inventory(self, item: Item):
        self.__inventory.append(item)

    def remove_from_inventory(self, item: Item):
        self.__inventory.remove(item)
        # TODO: implement __eq__ for item
