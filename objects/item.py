#!/usr/bin/env python3
from enum import Enum


class ItemType(Enum):
    WEAPON = 0
    SHIELD = 1
    ARMOR = 2
    UTILITIES = 3

class Item(object):
    def __init__(self):
        super(Item, self).__init__()
        self.__type = ItemType.UTILITIES

        self.__name = ""
        self.__value = ""
        self.__type = ""

        self.__special = ""

    @property
    def name(self):
        return self.__name

    @property
    def value(self):
        return self.__value

    @property
    def type(self):
        return self.__type

    @property
    def special(self):
        return self.__special


class Weapon(Item):
    def __init__(self):
        super(Weapon, self).__init__()
        self.__type = ItemType.WEAPON

        self.__required_skill = ""
        self.__damage = ""
        self.__crit_mod = ""
        self.__crit_dmg = ""
        self.__crit_effect = ""


class Sword(Weapon):
    def __init__(self):
        super(Sword, self).__init__()

        self.__required_dual_wield_skill = ""


class TwoHandedSwort(Weapon):
    def __init__(self):
        super(Sword, self).__init__()


class Dagger(Weapon):
    def __init__(self):
        super(Dagger, self).__init__()

        self.__required_dual_wield_skill = ""


class Dagger(Weapon):
    def __init__(self):
        super(Dagger, self).__init__()

        self.__required_dual_wield_skill = ""
