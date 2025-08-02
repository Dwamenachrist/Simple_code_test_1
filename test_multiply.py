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

    # New test cases for edge cases
    def test_multiply_large_numbers(self):
        self.assertEqual(multiply_numbers(10**10, 10**10), 10**20)

    def test_multiply_non_numeric_string(self):
        with self.assertRaises(TypeError):
            multiply_numbers("string", 5)

    def test_multiply_non_numeric_list(self):
        with self.assertRaises(TypeError):
            multiply_numbers([1, 2, 3], 5)

    def test_multiply_non_numeric_dict(self):
        with self.assertRaises(TypeError):
            multiply_numbers({"key": "value"}, 5)

    def test_multiply_boolean_true(self):
        self.assertEqual(multiply_numbers(True, 5), 5)

    def test_multiply_boolean_false(self):
        self.assertEqual(multiply_numbers(False, 5), 0)

if __name__ == '__main__':
    unittest.main()