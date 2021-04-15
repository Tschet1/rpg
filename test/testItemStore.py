#!/usr/bin/env python3

import unittest

from item_store import ITEMS


class TestItemStore(unittest.TestCase):
    def test_store(self):
        self.assertGreater(len(ITEMS), 0)


if __name__ == '__main__':
    unittest.main()
