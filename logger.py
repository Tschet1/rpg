#!/usr/bin/env python3

from typing import Optional

class Logger(object):
    def __init__(self, name: Optional[str] = None, logfile: Optional[str] = None):
        super().__init__()
        self.name = name + ": " if name else ""
        self.logfile = logfile


    def log(self, message: str):
        if self.logfile:
            with open(self.logfile, "a") as fil:
                print(self.name + message, file=fil)
        print(self.name + message)
