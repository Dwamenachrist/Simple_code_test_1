import unittest
from multiply import multiply_numbers

class TestMultiplyEdgeCases(unittest.TestCase):

    def test_multiply_large_numbers(self):
        # Arrange
        a = 10**18
        b = 10**18
        # Act
        result = multiply_numbers(a, b)
        # Assert
        self.assertEqual(result, a * b)

    def test_multiply_floating_point(self):
        # Arrange
        a = 1.5
        b = 2.5
        # Act
        result = multiply_numbers(a, b)
        # Assert
        self.assertAlmostEqual(result, 3.75)

    def test_multiply_zero(self):
        # Act and Assert
        self.assertEqual(multiply_numbers(0, 5), 0)
        self.assertEqual(multiply_numbers(5, 0), 0)

if __name__ == '__main__':
    unittest.main()