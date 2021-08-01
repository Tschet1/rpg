#!/usr/bin/env python3

import re
from enum import Enum, auto
from die.dices import D2, D4, D6, D8, D10, D12, D20, D100


class DieComposition(object):
    def __init__(self, composition: str):
        self._comp = re.sub(r"([0-9])d([0-9])", r"\1*d\2", composition)
        self._comp = re.sub(r"([0-9]+)\(", r"\1*(", self._comp)
        self._comp = re.sub(r" *\* *", r" * ", self._comp)
        self._comp = re.sub(r" *\+ *", r" + ", self._comp)
        self._comp = re.sub(r" *\( *", r" ( ", self._comp)
        self._comp = re.sub(r" *\) *", r" ) ", self._comp)
        self._comp = re.sub(r" */ *", r" / ", self._comp)
        self._comp = self._comp.strip()

    def __str__(self):
        return self._comp

    def __repr__(self):
        return self._comp.replace(" ", "")

    class Operator(Enum):
        PLUS = auto()
        MINUS = auto()
        MULT = auto()
        DIV = auto()
        GROUP = auto()
        DIE = auto()

    def __int__(self):
        return int(self._to_num())

    def __float__(self):
        return float(self._to_num())

    def __add__(self, other):
        return DieComposition(f"{repr(self)} + {other}")

    def __sub__(self, other):
        return DieComposition(f"{repr(self)} - {other}")

    def __mul__(self, other):
        return DieComposition(f"({repr(self)}) * ({other})")

    def __truediv__(self, other):
        return DieComposition(f"({repr(self)}) / ({other})")

    def __eq__(self, other):
        return repr(self) == repr(other)

    def _to_num(self):
        expression = self._comp

        def roll(match):
            if(match.group(0) == 'd2'):
                return str(int(D2))
            elif(match.group(0) == 'd4'):
                return str(int(D4))
            elif(match.group(0) == 'd6'):
                return str(int(D6))
            elif(match.group(0) == 'd8'):
                return str(int(D8))
            elif(match.group(0) == 'd10'):
                return str(int(D10))
            elif(match.group(0) == 'd12'):
                return str(int(D12))
            elif(match.group(0) == 'd20'):
                return str(int(D20))
            elif(match.group(0) == 'd100'):
                return str(int(D100))
            else:
                raise Error("Invalid die expression")

        expression = re.sub(r"d[0-9]+", roll, expression)
        return eval(expression)
