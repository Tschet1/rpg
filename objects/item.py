#!/usr/bin/env python3
from enum import Enum
from die.dices import die
from typing import Union
from die.die_composition import DieComposition

class ItemType(Enum):
    WEAPON = 0
    SHIELD = 1
    ARMOR = 2
    UTILITIES = 3


class Item(object):
    def __init__(self, name: str, value: int, weight: int):
        super(Item, self).__init__()
        self.__type = ItemType.UTILITIES

        self.__name = name
        self.__value = value
        self.__type = ItemType.UTILITIES

        self.__weight = weight
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

    @property
    def weight(self):
        return self.__weight


class Weapon(Item):
    def __init__(self, name: str, value: int, weight: int, required_skill: int, damage: Union[die, DieComposition, str] , crit_chance: int, crit_mult: int, crit_effect: str, reach: int):
        super().__init__(name=name, value=value, weight=weight)
        self.__type = ItemType.WEAPON

        self.__required_skill = required_skill

        if type(damage) == DieComposition:
            self.__damage = damage
        else:
            self.__damage = DieComposition(str(damage))

        self.__crit_chance = crit_chance
        self.__crit_mult = crit_mult
        self.__crit_effect = crit_effect
        self.__reach = reach


class Sword(Weapon):
    def __init__(self, dual_wield_skill: int, *args, **kwargs):
        super().__init__(*args, reach=1, **kwargs)

        self.__required_dual_wield_skill = dual_wield_skill


class TwoHandedWeapon(Weapon):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Dagger(Weapon):
    def __init__(self, dual_wield_skill: int, *args, **kwargs):
        super().__init__(*args, reach=1, **kwargs)

        self.__required_dual_wield_skill = dual_wield_skill


class Whip(Weapon):
    def __init__(self, dual_wield_skill: int, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.__required_dual_wield_skill = dual_wield_skill


class Bow(Weapon):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Crossbow(Weapon):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class ThrowingWeapons(Weapon):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
