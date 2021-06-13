#!/usr/bin/env python3

import unittest
import pathlib
import objects.person as person
from objects.familytree import create_whole_family_tree, create_family_tree_with_head

class TestFamilyTree(unittest.TestCase):

    def test_tree(self):
        # create a family
        head = person.get_random_person(gender=person.Gender.MALE, name="Alpha")
        head.spouse = person.get_random_person(gender=person.Gender.FEMALE)

        for _ in range(3):
            child = person.get_random_person()
            for _ in range(3):
                child.add_child(person.get_random_person())
            head.add_child(child)

        filename_part = pathlib.Path("partial");
        create_family_tree_with_head(head, filename_part)
        print(f"Partial family tree saved in {filename_part}")

        filename_whole = pathlib.Path("whole");
        create_whole_family_tree(head, filename_whole)
        print(f"Whole family tree saved in {filename_whole}")


if __name__ == '__main__':
    unittest.main()
