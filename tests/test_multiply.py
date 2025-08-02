import unittest
from multiply import multiply_numbers

class TestMultiplyNumbers(unittest.TestCase):

    def setUp(self):
        # Setup code can be placed here if needed
        pass

    def test_multiply_positive_numbers(self):
        """Test multiplication of two positive numbers."""
        self.assertEqual(multiply_numbers(3, 5), 15)

    def test_multiply_negative_number(self):
        """Test multiplication of a positive and a negative number."""
        self.assertEqual(multiply_numbers(-2, 3), -6)

    def test_multiply_zero(self):
        """Test multiplication with zero."""
        self.assertEqual(multiply_numbers(0, 5), 0)
        self.assertEqual(multiply_numbers(5, 0), 0)

    def test_multiply_floats(self):
        """Test multiplication of float numbers."""
        self.assertAlmostEqual(multiply_numbers(2.5, 4), 10.0)

    def test_multiply_large_numbers(self):
        """Test multiplication of large numbers."""
        self.assertEqual(multiply_numbers(1000000, 1000000), 1000000000000)

    def test_multiply_edge_cases(self):
        """Test edge cases such as multiplication by 1."""
        self.assertEqual(multiply_numbers(1, 100), 100)
        self.assertEqual(multiply_numbers(100, 1), 100)

    def tearDown(self):
        # Teardown can be implemented if needed
        pass

if __name__ == '__main__':
    unittest.main()