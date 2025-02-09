import unittest

from src.example import add_number,sub_number

class Test_Example(unittest.TestCase):
    def test_add_number(self):
        self.assertEqual(add_number(100,200),300)
        
    def test_add_number(self):
        self.assertEqual(sub_number(300,200),100)
        
        
if __name__ == "__main__":
    unittest.main()