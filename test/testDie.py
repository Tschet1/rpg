#!/usr/bin/env python3

import unittest

from die.dices import *


class TestDie(unittest.TestCase):

    def test_roll(self):
        dices_limits = [(D4, 4), (D6, 6), (D8, 8), (D10, 10),
                        (D12, 12), (D20, 20), (D100, 100)]

        for i in range(1000):
            for d, limit in dices_limits:
                result = int(d)
                self.assertGreaterEqual(result, 1)
                self.assertLessEqual(result, limit)

    def test_roll_mult(self):
        dices_limits = [(D4, 4), (D6, 6), (D8, 8), (D10, 10),
                        (D12, 12), (D20, 20), (D100, 100)]

        for i in range(1000):
            for d, limit in dices_limits:
                result = 2*d
                self.assertGreaterEqual(result, 2)
                self.assertLessEqual(result, limit*2)

    def test_roll_math(self):
        dices_limits = [(D4, 4), (D6, 6), (D8, 8), (D10, 10),
                        (D12, 12), (D20, 20), (D100, 100)]

        for i in range(1000):
            for d, limit in dices_limits:
                result = 2 * d + 3
                self.assertGreaterEqual(result, 5)
                self.assertLessEqual(result, limit*2+3)

        for i in range(1000):
            for d, limit in dices_limits:
                result = 3 + d * 2
                self.assertGreaterEqual(result, 5)
                self.assertLessEqual(result, limit*2+3)

    def test_str(self):
        dices_names = [(D4, "d4"), (D6, "d6"), (D8, "d8"),
                       (D10, "d10"), (D12, "d12"), (D20, "d20"), (D100, "d100")]

        for d, name in dices_names:
            self.assertEqual(str(d), name)


if __name__ == '__main__':
    unittest.main()
