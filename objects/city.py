#!/usr/bin/env python3

class City(object):
    def __init__(self):
        super().__init__()
        self.__name = 'Glimmerstadt'

    @property
    def name(self):
        return self.__name

    def __str__(self):
        return self.name
