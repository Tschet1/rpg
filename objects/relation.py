#!/usr/bin/env python3

from enum import IntEnum
from .person import Person

class Opinion(IntEnum):
    ABNEIGUNG = -3
    NEGATIV = -2
    GENERVT = -1
    ERFREUT = 1
    POSITIV = 2
    BEGEISTERT = 3


class Relation(object):
    def __init(self, towards_person: Person, reason: str, effect: Opinion):
        super().__init__()

        self.__towards = towards_person
        self.__reason = reason
        self.__effect = effect

    @property
    def towards(self):
        return self.__towards

    @property
    def reason(self):
        return self.__reason

    @property
    def effect(self):
        return self.__effect
