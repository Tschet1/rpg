#!/usr/bin/env python3

import unittest

from objects.names import *
from objects.person import Gender

class TestNames(unittest.TestCase):
    def test_names(self):
        name = get_random_last_name()
        self.assertGreater(len(name), 0)

        for gender in [Gender.FEMALE, Gender.MALE]:
            name = get_random_first_name(gender)
            self.assertGreater(len(name), 0)
            fname, lname = get_random_name(gender)
            self.assertGreater(len(fname), 0)
            self.assertGreater(len(lname), 0)
            print(f"Picked random name {fname} {lname}")
