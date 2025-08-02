import unittest
from your_module import multiply_numbers  # Adjust import according to your module structure

class TestMultiplyNumbers(unittest.TestCase):

    def test_multiply_positive_numbers(self):
        self.assertEqual(multiply_numbers(2, 3), 6)

    def test_multiply_negative_numbers(self):
        self.assertEqual(multiply_numbers(-2, -3), 6)

    def test_multiply_positive_and_negative(self):
        self.assertEqual(multiply_numbers(2, -3), -6)

    def test_multiply_by_zero(self):
        self.assertEqual(multiply_numbers(0, 10), 0)

    def test_multiply_floats(self):
        self.assertAlmostEqual(multiply_numbers(2.5, 4), 10.0)

if __name__ == '__main__':
    unittest.main()