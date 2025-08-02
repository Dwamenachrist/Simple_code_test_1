import unittest
from multiply import multiply_numbers

class TestMultiplyNumbers(unittest.TestCase):

    def test_standard_multiplication(self):
        """
        Test standard case of multiplication.
        For example: multiply_numbers(2, 3) should return 6.
        """
        self.assertEqual(multiply_numbers(2, 3), 6)
        self.assertEqual(multiply_numbers(-1, 5), -5)
        self.assertEqual(multiply_numbers(0, 10), 0)

    def test_edge_case_multiplying_by_zero(self):
        """
        Test cases multiplying by zero.
        For example: multiply_numbers(0, 10) and multiply_numbers(0, 0) should return 0.
        """
        self.assertEqual(multiply_numbers(0, 10), 0)
        self.assertEqual(multiply_numbers(0, 0), 0)

    def test_edge_case_multiply_zero_negative(self):
        """
        Testing where one of the inputs is negative.
        For example: multiply_numbers(-5, 0) should return 0.
        """
        self.assertEqual(multiply_numbers(-5, 0), 0)

    def test_non_numeric_inputs(self):
        """
        Test cases with non-numeric inputs should raise TypeError.
        Examples:
        - multiply_numbers('a', 2) 
        - multiply_numbers(None, 2) 
        """
        with self.assertRaises(TypeError):
            multiply_numbers('a', 2)
        with self.assertRaises(TypeError):
            multiply_numbers(None, 2)
        with self.assertRaises(TypeError):
            multiply_numbers(5, 'b')

if __name__ == '__main__':
    unittest.main()