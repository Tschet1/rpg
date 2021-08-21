#!/usr/bin/env python3

class Logger(object):
    def __init__(self, name: str):
        super().__init__()
        self.name = name

    def log(self, message: str):
        print(self.name + ":" + message)
