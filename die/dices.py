#!/usr/bin/env python3
from random import randint
from abc import ABC, abstractmethod


class die(ABC):
    @classmethod
    @abstractmethod
    def die_sides(cls):
        ...

    def __mul__(self, other):
        return int(self) * other

    def __rmul__(self, other):
        return int(self) * other

    def __int__(self):
        return randint(1, self.__class__().die_sides())

    def __str__(self):
        return f"d{self.__class__().die_sides()}"


class d20(die):
    @classmethod
    def die_sides(cls):
        return 20


class d12(die):
    @classmethod
    def die_sides(cls):
        return 12


class d10(die):
    @classmethod
    def die_sides(cls):
        return 10


class d8(die):
    @classmethod
    def die_sides(cls):
        return 8


class d6(die):
    @classmethod
    def die_sides(cls):
        return 6


class d4(die):
    @classmethod
    def die_sides(cls):
        return 4


class d100(die):
    @classmethod
    def die_sides(cls):
        return 100


class d2(die):
    @classmethod
    def die_sides(cls):
        return 2

    @classmethod
    def roll(cls):
        return super().roll() - 1

    def __int__(self):
        return randint(0, self.__class__().die_sides() - 1)


D20 = d20()
D12 = d12()
D10 = d10()
D8 = d8()
D6 = d6()
D4 = d4()
D100 = d100()
D2 = d2()
