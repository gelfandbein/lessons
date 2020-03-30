import unittest
from calculator import Calculator

"""
Should be userd with coverage
coverage run --omit=test_calculator.py -m unittest test_calculator
"""

class TestTVController(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_calc_name(self):
        calc = Calculator("My Calculator")
        self.assertEqual(calc.name, "My Calculator")

    def test_add(self):
        cases = [
            {"in": (2, 2), "out": 4},
            {"in": (2, 3), "out": 5},
        ]

        for case in cases:
            self.assertEqual(self.calc.add(case["in"][0], case["in"][1]), case["out"])
        # self.assertEqual(self.calc.add(2, 2), 4)
        # self.assertNotEqual(self.calc.add(3, 3), 7)

    def test_minus(self):
        self.assertEqual(self.calc.minus(3, 3), 0)
        self.assertNotEqual(self.calc.minus(2, 2), 1)

    def test_sum(self):
        self.assertEqual(self.calc.sum(3, 3, 4), 10)
        self.assertNotEqual(self.calc.sum(3, 3, 4), 11)

    def test_div(self):
        res = self.calc.div(6, 3)
        self.assertEqual(res, 2, "6 / 3 should be 2")

    def test_div_error(self):
        with self.assertRaises(ValueError):
            self.calc.div(6, 0)
            # res = self.calc.div(6, 0)
            # self.assertEqual(res, None, "Division by zero")



if __name__ == "__main__":
    unittest.main()

