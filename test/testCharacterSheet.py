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

        c.attributes['strength'].increase_value()
        c.abilities['Running'].increase_value()
        c.abilities['Read'].attribut.increase_value()
        c.abilities['Read'].increase_value()

        self.assertEqual(c.attributes['strength'].value, 1)
        self.assertEqual(c.abilities['Running'].value, 1)
        self.assertEqual(c.attributes['intelligence'].value, 1)
        self.assertEqual(c.abilities['Read'].value, 1)

        c.attributes['strength'].decrease_value()
        c.abilities['Running'].decrease_value()

        self.assertEqual(c.attributes['strength'].value, 0)
        self.assertEqual(c.abilities['Running'].value, 0)

    def test_limit_violation(self):
        c = mod_system()

        with self.assertRaises(ValueError):
            c.abilities['Running'].increase_value()

        with self.assertRaises(ValueError):
            c.abilities['Swimming'].decrease_value()

        with self.assertRaises(ValueError):
            c.attributes['strength'].decrease_value()

        self.assertEqual(c.attributes['strength'].value, 0)
        self.assertEqual(c.abilities['Running'].value, 0)
        self.assertEqual(c.abilities['Swimming'].value, 0)

    def test_connections(self):
        c = mod_system()
        self.assertEqual(c.attributes['strength'].abilities, {
            "Running": c.abilities['Running'],
            "Swimming": c.abilities['Swimming'],
            "Climbing": c.abilities['Climbing']
        })

        self.assertEqual(c.strength.abilities, {
            "Running": c.Running,
            "Swimming": c.Swimming,
            "Climbing": c.Climbing
        })

        self.assertEqual(
            c.abilities['Running'].attribut, c.attributes['strength'])
        self.assertEqual(c.Running.attribut, c.strength)

    def test_bonus(self):
        c = mod_system()

        c.abilities['Running'].add_bonus(3, "Test")
        c.abilities['Swimming'].add_malus(3, "Test")

        self.assertEqual(c.abilities['Running'].value, 3)
        self.assertEqual(c.abilities['Swimming'].value, -3)

        with self.assertRaises(ValueError):
            c.abilities['Climbing'].add_bonus(-3, "Test 2")

        self.assertEqual(c.abilities['Climbing'].value, 0)

        with self.assertRaises(ValueError):
            c.abilities['Climbing'].add_malus(-3, "Test 2")

        self.assertEqual(c.abilities['Climbing'].value, 0)

        c.abilities['Running'].add_bonus(3, "Test")
        c.abilities['Swimming'].add_malus(3, "Test")

        self.assertEqual(c.abilities['Running'].value, 6)
        self.assertEqual(c.abilities['Swimming'].value, -6)

        c.abilities['Swimming'].add_bonus(3, "Test")
        self.assertEqual(c.abilities['Swimming'].value, -3)

    def test_internal_objects(self):
        c = mod_system()

        c.abilities['Read'].attribut.increase_value()
        c.abilities['Read'].increase_value()
        self.assertEqual(c.abilities['Read'].attribut, c.intelligence)
        self.assertEqual(c.abilities['Read'], c.Read)
        self.assertEqual(
            str(c.abilities['Read'].attribut), str(c.intelligence))
        self.assertEqual(str(c.abilities['Read']), str(c.Read))
        self.assertEqual(
            int(c.abilities['Read'].attribut), int(c.intelligence))
        self.assertEqual(int(c.abilities['Read']), int(c.Read))


if __name__ == '__main__':
    unittest.main()
