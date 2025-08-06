import unittest
from multiply import multiply_numbers

class TestEdgeCases(unittest.TestCase):

    def test_large_numbers(self):
        self.assertEqual(multiply_numbers(10000, 10000), 100000000)

    def test_one_negative_and_one_positive(self):
        self.assertEqual(multiply_numbers(-10, 10), -100)
        self.assertEqual(multiply_numbers(10, -10), -100)

if __name__ == '__main__':
    unittest.main()