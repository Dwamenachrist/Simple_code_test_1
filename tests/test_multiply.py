import unittest
from multiply import multiply_numbers

class TestMultiplyNumbers(unittest.TestCase):

    def test_multiply_positive_numbers(self):
        self.assertEqual(multiply_numbers(2, 3), 6)

    def test_multiply_negative_numbers(self):
        self.assertEqual(multiply_numbers(-2, -3), 6)

    def test_multiply_positive_negative(self):
        self.assertEqual(multiply_numbers(2, -3), -6)

    def test_multiply_by_zero(self):
        self.assertEqual(multiply_numbers(0, 5), 0)
        self.assertEqual(multiply_numbers(5, 0), 0)

    def test_multiply_large_numbers(self):
        self.assertEqual(multiply_numbers(10000, 10000), 100000000)

    def test_multiply_floats(self):
        self.assertAlmostEqual(multiply_numbers(2.5, 4), 10.0)

if __name__ == '__main__':
    unittest.main()