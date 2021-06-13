#!/usr/bin/env python3

import unittest

from my_system import System


class mod_system(System):
    @property
    def attribute_ability_mapping(self) -> dict:
        return {
            "strength": ["Running", "Swimming", "Climbing"],
            "intelligence": ["Hustle", "Read"]
        }


class TestCharactersheet(unittest.TestCase):
    def test_limits(self):
        c = mod_system()

        c.attributes[0].increase_value()
        c.abilities[0].increase_value()
        c.abilities[-1].attribut.increase_value()
        c.abilities[-1].increase_value()

        self.assertEqual(c.attributes[0].value, 1)
        self.assertEqual(c.abilities[0].value, 1)
        self.assertEqual(c.attributes[-1].value, 1)
        self.assertEqual(c.abilities[-1].value, 1)

        c.attributes[0].decrease_value()
        c.abilities[0].decrease_value()

        self.assertEqual(c.attributes[0].value, 0)
        self.assertEqual(c.abilities[0].value, 0)

    def test_limit_violation(self):
        c = mod_system()

        with self.assertRaises(ValueError):
            c.abilities[0].increase_value()

        with self.assertRaises(ValueError):
            c.abilities[1].decrease_value()

        with self.assertRaises(ValueError):
            c.attributes[0].decrease_value()

        self.assertEqual(c.attributes[0].value, 0)
        self.assertEqual(c.abilities[0].value, 0)
        self.assertEqual(c.abilities[1].value, 0)

    def test_bonus(self):
        c = mod_system()

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

    def test_internal_objects(self):
        c = mod_system()

        c.abilities[-1].attribut.increase_value()
        c.abilities[-1].increase_value()
        self.assertEqual(c.abilities[-1].attribut, c.intelligence)
        self.assertEqual(c.abilities[-1], c.Read)
        self.assertEqual(str(c.abilities[-1].attribut), str(c.intelligence))
        self.assertEqual(str(c.abilities[-1]), str(c.Read))
        self.assertEqual(int(c.abilities[-1].attribut), int(c.intelligence))
        self.assertEqual(int(c.abilities[-1]), int(c.Read))


if __name__ == '__main__':
    unittest.main()
