import unittest
from multiply import multiply_numbers

class TestMultiplyNumbers(unittest.TestCase):
    """
    Test cases for the multiply_numbers function.
    """

    def test_multiply_positive_numbers(self):
        """
        Test multiplication of two positive numbers.
        """
        self.assertEqual(multiply_numbers(3, 4), 12)
        self.assertEqual(multiply_numbers(10, 5), 50)

    def test_multiply_negative_numbers(self):
        """
        Test multiplication of two negative numbers.
        """
        self.assertEqual(multiply_numbers(-3, -4), 12)
        self.assertEqual(multiply_numbers(-10, -5), 50)

    def test_multiply_negative_and_positive(self):
        """
        Test multiplication of a positive number and a negative number.
        """
        self.assertEqual(multiply_numbers(-3, 4), -12)
        self.assertEqual(multiply_numbers(10, -5), -50)

    def test_multiply_zero(self):
        """
        Test multiplication of any number with zero.
        """
        self.assertEqual(multiply_numbers(0, 10), 0)
        self.assertEqual(multiply_numbers(10, 0), 0)

    def test_multiply_large_numbers(self):
        """
        Test multiplication of large numbers.
        """
        self.assertEqual(multiply_numbers(100000, 100000), 10000000000)
        self.assertEqual(multiply_numbers(-100000, 100000), -10000000000)

if __name__ == '__main__':
    unittest.main()