#!/usr/bin/env python3

import unittest

from charactersheet.sheet import Charactersheet

class TestCharactersheet(unittest.TestCase):
    def test_limits(self):
        mapping = {
            "strength": ["Running", "Swimming", "Climbing"],
            "intelligence": ["Hustle", "Read"]
        }

        c = Charactersheet(mapping)

        c.atributes[0].increase_value()
        c.abilities[0].increase_value()
        c.abilities[-1].atribut.increase_value()
        c.abilities[-1].increase_value()

        self.assertEqual(c.atributes[0].value, 1)
        self.assertEqual(c.abilities[0].value, 1)
        self.assertEqual(c.atributes[-1].value, 1)
        self.assertEqual(c.abilities[-1].value, 1)

        c.atributes[0].decrease_value()
        c.abilities[0].decrease_value()

        self.assertEqual(c.atributes[0].value, 0)
        self.assertEqual(c.abilities[0].value, 0)

    def test_limit_violation(self):
        mapping = {
            "strength": ["Running", "Swimming", "Climbing"]
        }

        c = Charactersheet(mapping)

        with self.assertRaises(ValueError):
            c.abilities[0].increase_value()

        with self.assertRaises(ValueError):
            c.abilities[1].decrease_value()

        with self.assertRaises(ValueError):
            c.atributes[0].decrease_value()

        self.assertEqual(c.atributes[0].value, 0)
        self.assertEqual(c.abilities[0].value, 0)
        self.assertEqual(c.abilities[1].value, 0)

    def test_bonus(self):
        mapping = {
            "strength": ["Running", "Swimming", "Climbing"]
        }

        c = Charactersheet(mapping)

        c.abilities[0].add_bonus(3, "Test")
        c.abilities[1].add_malus(3, "Test")

        self.assertEqual(c.abilities[0].value, 3)
        self.assertEqual(c.abilities[1].value, -3)

        with self.assertRaises(ValueError):
            c.abilities[2].add_bonus(-3, "Test 2")

        self.assertEqual(c.abilities[2].value, 0)

        with self.assertRaises(ValueError):
            c.abilities[2].add_malus(-3, "Test 2")

        self.assertEqual(c.abilities[2].value, 0)

        c.abilities[0].add_bonus(3, "Test")
        c.abilities[1].add_malus(3, "Test")

        self.assertEqual(c.abilities[0].value, 6)
        self.assertEqual(c.abilities[1].value, -6)

        c.abilities[1].add_bonus(3, "Test")
        self.assertEqual(c.abilities[1].value, -3)

if __name__ == '__main__':
    unittest.main()
