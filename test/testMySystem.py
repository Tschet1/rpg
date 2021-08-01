#!/usr/bin/env python3

import unittest

from objects.person import get_random_person
from item_store import ITEMS

class TestMySystem(unittest.TestCase):
    def test_dmg(self):
        pers = get_random_person()

        with self.assertRaises(Exception):
            dmg = pers.dmg

        pers.weapon = [it for it in ITEMS if it.name == "Holzschwert"][0]
        dmg = pers.dmg


if __name__ == '__main__':
    unittest.main()
