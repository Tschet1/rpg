#!/usr/bin/env python3

from objects.city import City


class Address(object):
    def __init__(self):
        super().__init__()
        self.__city = City()
        self.__address = ''

    @property
    def city(self):
        return self.__city

    @property
    def address(self):
        return self.__address

    def __str__(self):
        return f"{self.__address}, {self.__city}"
