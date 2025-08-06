import unittest
from multiply import multiply_numbers

class TestMultiplyNumbers(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(multiply_numbers(3, 4), 12)
        self.assertEqual(multiply_numbers(2, 5), 10)

    def test_negative_numbers(self):
        self.assertEqual(multiply_numbers(-2, -3), 6)
        self.assertEqual(multiply_numbers(-1, 5), -5)

    def test_zero(self):
        self.assertEqual(multiply_numbers(0, 5), 0)
        self.assertEqual(multiply_numbers(0, 0), 0)

if __name__ == '__main__':
    unittest.main()