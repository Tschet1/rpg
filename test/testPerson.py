#!/usr/bin/env python3

import unittest

from objects.person import *

class TestPerson(unittest.TestCase):
    def test_random_person(self):
        get_random_person()
