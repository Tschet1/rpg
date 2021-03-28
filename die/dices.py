#!/usr/bin/env python3
from random import randint
from abc import ABC, abstractmethod


class die(ABC):
    @classmethod
    @abstractmethod
    def die_sides(cls):
        ...

    @classmethod
    def roll(cls):
        return randint(1, cls.die_sides())


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
