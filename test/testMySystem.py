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
        self.assertEqual(dmg, pers.weapon.damage + 0)

        for i in range(20):
            pers.sheet.Einhandwaffen.increase_value()
            pers.sheet.Schwerter.increase_value()
            dmg = pers.dmg
            self.assertEqual(dmg, pers.weapon.damage +
                             pers.sheet.Schwerter.value // 5)

    def test_attack(self):
        pers = get_random_person()

        with self.assertRaises(Exception):
            at = pers.attack

        pers.weapon = [it for it in ITEMS if it.name == "Holzschwert"][0]

        at = pers.attack
        self.assertEqual(at, 0)

        for i in range(20):
            pers.sheet.Einhandwaffen.increase_value()
            pers.sheet.Schwerter.increase_value()
            at = pers.attack
            self.assertEqual(at, pers.sheet.Einhandwaffen.value + round(
                pers.sheet.Schwerter.value / len(pers.sheet.Einhandwaffen.abilities)))

        for i in range(20):
            pers.sheet.Dolche.increase_value()
            at = pers.attack
            self.assertEqual(at, pers.sheet.Einhandwaffen.value + round((pers.sheet.Schwerter.value +
                             pers.sheet.Dolche.value) / len(pers.sheet.Einhandwaffen.abilities)))


if __name__ == '__main__':
    unittest.main()
