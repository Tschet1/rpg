#!/usr/bin/env python3

import unittest
from timeline.fight import Fight
from objects.person import get_random_person


class TestFightTimeline(unittest.TestCase):
    def _add_person_with_agility(self, fight, agility):
        person = get_random_person()
        for i in range(agility):
            person.stats.Agilität.increase_value()
        fight.add_person(person)
        return person

    def test_basics(self):
        fi = Fight()
        person1 = self._add_person_with_agility(fi, 1)
        person2 = self._add_person_with_agility(fi, 10)

        pers = fi.get_next_combatant()
        self.assertEqual(pers, person1)
        pers = fi.get_next_combatant()
        self.assertEqual(pers, person2)
        pers = fi.get_next_combatant()
        self.assertEqual(pers, person2)

    def test_dies_fast(self):
        fi = Fight()
        person1 = self._add_person_with_agility(fi, 1)
        person2 = self._add_person_with_agility(fi, 10)
        fi.remove_combatant(person1)

        pers = fi.get_next_combatant()
        self.assertEqual(pers, person2)
        self.assertEqual(len(fi.future), 1)

        fi = Fight()
        person1 = self._add_person_with_agility(fi, 1)
        person2 = self._add_person_with_agility(fi, 10)
        fi.remove_combatant(person2)

        pers = fi.get_next_combatant()
        self.assertEqual(pers, person1)
        self.assertEqual(len(fi.future), 1)

    def test_die_all(self):
        fi = Fight()
        person1 = self._add_person_with_agility(fi, 1)
        person2 = self._add_person_with_agility(fi, 10)
        fi.remove_combatant(person1)
        fi.remove_combatant(person2)

        with self.assertRaises(Exception):
            pers = fi.get_next_combatant()

    def test_dies(self):
        fi = Fight()
        person1 = self._add_person_with_agility(fi, 1)
        person2 = self._add_person_with_agility(fi, 10)

        pers = fi.get_next_combatant()
        self.assertEqual(pers, person1)
        pers = fi.get_next_combatant()
        self.assertEqual(pers, person2)
        pers = fi.get_next_combatant()

        # dies
        self.assertEqual(len(fi.future), 2)
        fi.remove_combatant(person2)
        self.assertEqual(len(fi.future), 1)

        pers = fi.get_next_combatant()
        self.assertEqual(pers, person1)
        pers = fi.get_next_combatant()
        self.assertEqual(pers, person1)
        pers = fi.get_next_combatant()
        self.assertEqual(pers, person1)


if __name__ == '__main__':
    unittest.main()
