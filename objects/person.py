#!/usr/bin/env python3
from __future__ import annotations
from enum import Enum
from .address import Address
from my_system import System
from .relation import Opinion, Relation
from .item import Item, Weapon
from typing import Type
import objects.names as names
import random
import die.dices as die
from objects.gender import Gender


class SexualOrientation(Enum):
    HOMOSEXUAL = 1
    HETEROSEXUAL = 2
    ASEXUAL = 3

    def __str__(self):
        return self.name


class Race(Enum):
    HUMAN = 1
    DWARF = 2
    NIXE = 3
    ELF = 4

    def __str__(self):
        return self.name


class Language(Enum):
    DEF = 1

    def __str__(self):
        return self.name


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

    def __str__(self):
        return self.name

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
        self.__children = []
        self.__spouse = None
        self.__pets = None

        self.__relations = []

        self.__notes = []

        self.__sheet = System()
        self.__sexual_orientation = sexorient

        self.__inventroy = {}

        self.__age = age
        self.__is_alive = True

        # TODO: getters / setters
        self.__hp = self.__sheet.max_life

        # TODO:
        # hp/mana usw.
        # attack, defense, weight of inventory

    @property
    def stats(self):
        return self.__sheet

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
    def spouse(self):
        return self.__spouse

    @spouse.setter
    def spouse(self, spouse: Person):
        self.__spouse = spouse

    @property
    def children(self):
        return self.__children

    def add_child(self, child: Person):
        self.__children.append(child)

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age: int):
        self.__age = age

    @property
    def weapon(self):
        return self.__sheet.weapon

    @weapon.setter
    def weapon(self, weapon):
        if(not isinstance(weapon, Weapon)):
            raise Exception("Tried to equip something that is not a weapon")
        self.__sheet.weapon = weapon

    @property
    def sheet(self):
        return self.__sheet

    @property
    def is_alive(self):
        return self.__is_alive

    def die(self):
        if not self.__is_alive:
            raise Exception("Already dead")
        self.__is_alive = False

    def revive(self):
        if self.__is_alive:
            raise Exception("Already alive")
        self.__is_alive = True

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
    def fight_speed(self):
        return self.__sheet.fight_speed

    @property
    def dmg(self):
        return self.__sheet.dmg

    @property
    def attack(self):
        return self.__sheet.attack

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


def get_random_person(**kwargs) -> Person:
    def random_char(kwargs: dict, char: str, die: Type(die), rand_fun):
        if not char in kwargs:
            print(f"create random {char}")
            if die is not None:
                res = int(die)
                kwargs[char] = rand_fun(res)
                print(f"Roll {str(die)} -> {res} : {kwargs[char]}")
            else:
                kwargs[char] = rand_fun()
                print(f"{kwargs[char]}")

    print("start creating random person")
    random_char(kwargs, "gender", die.D20,
                lambda res: Gender.MALE if res < 19 else Gender.FEMALE)
    random_char(kwargs, "name", None, lambda: ' '.join(
        names.get_random_name(kwargs['gender'])))
    random_char(kwargs, "age", die.D20, lambda res: 18 + res)
    random_char(kwargs, "address", None, lambda: Address())

    def pick_race(rand: int):
        if(rand < 18):
            return Race.HUMAN
        elif(rand < 19):
            return Race.DWARF
        else:
            return Race.ELF

    random_char(kwargs, "race", die.D20, pick_race)
    random_char(kwargs, "height", die.D20, lambda res: 160 + 2*res)
    random_char(kwargs, "languages", None, lambda: [])
    random_char(kwargs, "profession", None,
                lambda:  random.choice(list(Profession)))
    random_char(kwargs, "sexorient", die.D20, lambda res: SexualOrientation.HETEROSEXUAL if res <
                17 else SexualOrientation.HOMOSEXUAL if res < 19 else SexualOrientation.ASEXUAL)

    # TODO: define additional characteristics and make some things more probable than others

    return Person(**kwargs)
