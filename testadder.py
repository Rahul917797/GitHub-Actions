# test_adder.py

import unittest
from adder import add

class TestAddFunction(unittest.TestCase):
    def test_positive(self):
        self.assertEqual(add(2, 3), 5)

    def test_negative(self):
        self.assertEqual(add(-1, -1), -2)

    def test_mixed(self):
        self.assertEqual(add(-1, 1), 0)

if __name__ == '__main__':
    unittest.main()

