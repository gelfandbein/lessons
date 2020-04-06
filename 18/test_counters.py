import unittest

from counters import count_lines, count_chars

"""
Should be userd with coverage
coverage run --omit=test_tvcontroller.py -m unittest test_tvcontroller
"""


class Counters(unittest.TestCase):
    def setUp(self):
        self.debug = True

    def test_count_lines(self):
        self.assertEqual(count_lines("./counters.txt"), 3)

    def test_count_chars(self):
        self.assertEqual(count_chars("./counters.txt"), 44)


if __name__ == "__main__":
    # unittest.main()
    try:
        suite = unittest.TestLoader().loadTestsFromTestCase(Counters)
        unittest.TextTestRunner(verbosity=2).run(suite)
    except:
        print("Sorry, broken")
