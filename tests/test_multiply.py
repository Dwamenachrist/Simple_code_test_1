import unittest
from multiply import multiply_numbers

class TestMultiplyNumbers(unittest.TestCase):

    def test_multiply_positive_numbers(self):
        """Test multiplying two positive numbers."""
        self.assertEqual(multiply_numbers(3, 4), 12)

    def test_multiply_negative_numbers(self):
        """Test multiplying two negative numbers."""
        self.assertEqual(multiply_numbers(-3, -4), 12)

    def test_multiply_positive_negative(self):
        """Test multiplying a positive and a negative number."""
        self.assertEqual(multiply_numbers(3, -4), -12)

    def test_multiply_with_zero(self):
        """Test multiplying by zero."""
        self.assertEqual(multiply_numbers(0, 5), 0)
        self.assertEqual(multiply_numbers(5, 0), 0)

    def test_multiply_floats(self):
        """Test multiplying two float numbers."""
        self.assertAlmostEqual(multiply_numbers(2.5, 3.2), 8.0)

    def test_multiply_large_numbers(self):
        """Test multiplying large numbers."""
        self.assertEqual(multiply_numbers(100000, 200), 20000000)

if __name__ == '__main__':
    unittest.main()