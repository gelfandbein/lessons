import unittest
from unittest.mock import patch
import mock
import io
import sys

from tvcontroller import TVController

"""
Should be userd with coverage
coverage run --omit=test_tvcontroller.py -m unittest test_tvcontroller
"""

class TestTVController(unittest.TestCase):
    def setUp(self):
        self.tvctl = TVController()
        self.debug = True

    def tearDown(self):
        pass

    def test_init(self):
        self.assertEqual(self.tvctl.name, "My TVController")
        self.assertEqual(self.tvctl.list, ["BBC", "Discovery", "TV1000"])
        self.assertEqual(self.tvctl.status, 0)
        self.assertEqual(self.tvctl.channel, 0)

    #@unittest.skip("skipping right now")
    # def test_test(self):
    #     self.assertEqual(self.tvctl.status, 0)
    #     self.assertFalse(self.tvctl.status == None)
    #     with mock.patch('builtins.input', return_value="y"):
    #         assert self.tvctl.test() != "Hardware test passed!"

    @patch('builtins.input', return_value='y') # side_effect=["y", "yes"])
    def test_switch(self, v):
        # channel = self.tvctl.channel
        saved_stdout = sys.stdout
        self.assertRaises(KeyboardInterrupt)
            with self.assertRaises():
        try:
            out = io.StringIO()
            sys.stdout = out
            self.tvctl.switch(self.tvctl.channel)
            output = out.getvalue().strip()
            self.assertEqual(output, "Now you watch the BBC channel. You have BBC, Discovery, TV1000 channels.")
        finally:
            sys.stdout = saved_stdout


    def test_switch(self):
        self.assertFalse(self.tvctl.channel > len(self.tvctl.list))

    def test_main(self):
        pass
        #self.assertEqual('p', 'n', "Oops! Sorry!")



if __name__ == "__main__":
    #unittest.main()
    suite = unittest.TestLoader().loadTestsFromTestCase(TestTVController)
    unittest.TextTestRunner(verbosity=2).run(suite)
