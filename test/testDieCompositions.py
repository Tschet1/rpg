#!/usr/bin/env python3

import unittest

from die.die_composition import DieComposition


class TestDieComposition(unittest.TestCase):
    def test_string_rep(self):
        self.assertEqual(str(DieComposition("20")), "20")
        self.assertEqual(str(DieComposition("1d20")), "1 * d20")
        self.assertEqual(str(DieComposition("2+1d6")), "2 + 1 * d6")
        self.assertEqual(str(DieComposition("5*d2")), "5 * d2")
        self.assertEqual(str(DieComposition("2 + 1d20 * 5")),
                         "2 + 1 * d20 * 5")
        self.assertEqual(str(DieComposition("2(d5+3)")), "2 * ( d5 + 3 )")
        self.assertEqual(str(DieComposition("2d5+3d3")), "2 * d5 + 3 * d3")
        self.assertEqual(str(DieComposition("2*(2d14)/3")),
                         "2 * ( 2 * d14 ) / 3")
        self.assertEqual(str(DieComposition("2*(5+(2d14+3)*2)/3")),
                         "2 * ( 5 + ( 2 * d14 + 3 ) * 2 ) / 3")

    def test_eval_int(self):
        test_vector = [
            ("20", 20, 20),
            ("1d20", 1, 20),
            ("2+1d6", 3, 8),
            ("5*d2", 0, 5),
            ("2 + 1d20 * 5", 7, 102),
            ("3*(2d12)/3", 2, 24),
            ("2(d6+3)", 8, 18),
            ("(1d4+(2d8+3))/2", 3, 11),  # casting to int
        ]
        repetitions = 1000

        for pat, mi, ma in test_vector:
            min_reached = False
            max_reached = False
            for _ in range(repetitions):
                val = int(DieComposition(pat))
                self.assertLessEqual(
                    val, ma, f"pattern {pat} too big (limit {ma})")
                self.assertGreaterEqual(
                    val, mi, f"pattern {pat} too small (limit {mi})")
                min_reached = min_reached or val == mi
                max_reached = max_reached or val == ma

            self.assertTrue(
                min_reached, f"Min value {mi} for pattern {pat} not hit in {repetitions} rounds")
            self.assertTrue(
                max_reached, f"Max value {ma} for pattern {pat} not hit in {repetitions} rounds")

    def test_eval_float(self):
        test_vector = [
            ("20", 20, 20),
            ("1d20", 1, 20),
            ("2+1d6", 3, 8),
            ("5*d2", 0, 5),
            ("2 + 1d20 * 5", 7, 102),
            ("3*(2d12)/3", 2, 24),
            ("2(d6+3)", 8, 18),
            ("(1d4+(2d8+3))/2", 3, 11.5),
        ]
        repetitions = 1000

        for pat, mi, ma in test_vector:
            min_reached = False
            max_reached = False
            for _ in range(repetitions):
                val = float(DieComposition(pat))
                self.assertLessEqual(
                    val, ma, f"pattern {pat} too big (limit {ma})")
                self.assertGreaterEqual(
                    val, mi, f"pattern {pat} too small (limit {mi})")
                min_reached = min_reached or val == mi
                max_reached = max_reached or val == ma

            self.assertTrue(
                min_reached, f"Min value {mi} for pattern {pat} not hit in {repetitions} rounds")
            self.assertTrue(
                max_reached, f"Max value {ma} for pattern {pat} not hit in {repetitions} rounds")

    def test_raises(self):
        with self.assertRaises(Exception):
            int(DieComposition("2(d5+3)"))

    def test_arith_plus(self):
        test_vector = [
            ("2+1d6", 3, 8),
            ("3*(2d12)/3", 2, 24),
            ("(1d4+(2d8+3))/2", 3, 11.5),
        ]
        repetitions = 1000

        for pat, mi, ma in test_vector:
            min_reached = False
            max_reached = False
            for _ in range(repetitions):
                comp = DieComposition(pat) + 5
                cmi = mi + 5
                cma = ma + 5
                val = float(comp)
                self.assertLessEqual(
                    val, cma, f"pattern {pat} too big (limit {cma})")
                self.assertGreaterEqual(
                    val, cmi, f"pattern {pat} too small (limit {cmi})")
                min_reached = min_reached or val == cmi
                max_reached = max_reached or val == cma

            self.assertTrue(
                min_reached, f"Min value {cmi} for pattern {pat} not hit in {repetitions} rounds")
            self.assertTrue(
                max_reached, f"Max value {cma} for pattern {pat} not hit in {repetitions} rounds")

    def test_arith_minus(self):
        test_vector = [
            ("2+1d6", 3, 8),
            ("3*(2d12)/3", 2, 24),
            ("(1d4+(2d8+3))/2", 3, 11.5),
        ]
        repetitions = 1000

        for pat, mi, ma in test_vector:
            min_reached = False
            max_reached = False
            for _ in range(repetitions):
                comp = DieComposition(pat) - 10
                cmi = mi - 10
                cma = ma - 10
                val = float(comp)
                self.assertLessEqual(
                    val, cma, f"pattern {pat} too big (limit {cma})")
                self.assertGreaterEqual(
                    val, cmi, f"pattern {pat} too small (limit {cmi})")
                min_reached = min_reached or val == cmi
                max_reached = max_reached or val == cma

            self.assertTrue(
                min_reached, f"Min value {cmi} for pattern {pat} not hit in {repetitions} rounds")
            self.assertTrue(
                max_reached, f"Max value {cma} for pattern {pat} not hit in {repetitions} rounds")

    def test_arith_mult(self):
        test_vector = [
            ("2+1d6", 3, 8),
            ("3*(2d12)/3", 2, 24),
            ("(1d4+(2d8+3))/2", 3, 11.5),
        ]
        repetitions = 1000

        for pat, mi, ma in test_vector:
            min_reached = False
            max_reached = False
            for _ in range(repetitions):
                comp = DieComposition(pat) * 5
                cmi = mi * 5
                cma = ma * 5
                val = float(comp)
                self.assertLessEqual(
                    val, cma, f"pattern {pat} too big (limit {cma})")
                self.assertGreaterEqual(
                    val, cmi, f"pattern {pat} too small (limit {cmi})")
                min_reached = min_reached or val == cmi
                max_reached = max_reached or val == cma

            self.assertTrue(
                min_reached, f"Min value {cmi} for pattern {pat} not hit in {repetitions} rounds")
            self.assertTrue(
                max_reached, f"Max value {cma} for pattern {pat} not hit in {repetitions} rounds")

    def test_arith_div(self):
        test_vector = [
            ("2+1d6", 3, 8),
            ("3*(2d12)/3", 2, 24),
            ("(1d4+(2d8+3))/2", 3, 11.5),
        ]
        repetitions = 1000

        for pat, mi, ma in test_vector:
            min_reached = False
            max_reached = False
            for _ in range(repetitions):
                comp = DieComposition(pat) / 2
                cmi = mi / 2
                cma = ma / 2
                val = float(comp)
                self.assertLessEqual(
                    val, cma, f"pattern {pat} too big (limit {cma})")
                self.assertGreaterEqual(
                    val, cmi, f"pattern {pat} too small (limit {cmi})")
                min_reached = min_reached or val == cmi
                max_reached = max_reached or val == cma

            self.assertTrue(
                min_reached, f"Min value {cmi} for pattern {pat} not hit in {repetitions} rounds")
            self.assertTrue(
                max_reached, f"Max value {cma} for pattern {pat} not hit in {repetitions} rounds")

    def test_arith_chain(self):
        comp = (DieComposition("2+1d6") + DieComposition("2+2d6") -
                DieComposition("1d2")) * DieComposition("1+5d2") / DieComposition("1d8 + 2")
        self.assertEqual(str(comp).replace(" ", ""),
                         "((2+1*d6+2+2*d6-1*d2)*(1+5*d2))/(1*d8+2)")


if __name__ == '__main__':
    unittest.main()
