#!/usr/bin/env python3

import unittest
from logger import Logger

class TestLogger(unittest.TestCase):
    def testLogNoFile(self):
        log = Logger()
        log.log("Hallo")


    def testLogFile(self):
        logfile = "logfile"

        with open(logfile, "w") as fil:
            fil.write("START\n")

        log = Logger(logfile=logfile)
        log.log("Hallo1")
        log.log("Hallo2")

        with open(logfile, "r") as fil:
            lines = fil.readlines()
            self.assertEqual(3, len(lines))
            self.assertEqual("START\n", lines[0])
            self.assertEqual("Hallo1\n", lines[1])
            self.assertEqual("Hallo2\n", lines[2])


    def testLogFileWithName(self):
        logfile = "logfile"

        with open(logfile, "w") as fil:
            fil.write("START\n")

        log = Logger(logfile=logfile, name="Test")
        log.log("Hallo1")
        log.log("Hallo2")

        with open(logfile, "r") as fil:
            lines = fil.readlines()
            self.assertEqual(3, len(lines))
            self.assertEqual("START\n", lines[0])
            self.assertEqual("Test: Hallo1\n", lines[1])
            self.assertEqual("Test: Hallo2\n", lines[2])
