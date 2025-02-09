import sys
import os
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.example import add_number, sub_number

class Test_Example(unittest.TestCase):
    def test_add_number(self):
        self.assertEqual(add_number(100, 200), 300)

    def test_sub_number(self): 
        self.assertEqual(sub_number(300, 200), 100)

if __name__ == "__main__":
    unittest.main()
