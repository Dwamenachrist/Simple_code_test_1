import unittest
from multiply import multiply_numbers

class TestInvalidInputs(unittest.TestCase):

    def test_multiply_string_inputs(self):
        # Test multiplying with string input
        with self.assertRaises(TypeError):
            multiply_numbers('a', 5)

    def test_multiply_none_values(self):
        # Test multiplying with None
        with self.assertRaises(TypeError):
            multiply_numbers(None, 10)

    def test_multiply_list_input(self):
        # Test multiplying with list input
        with self.assertRaises(TypeError):
            multiply_numbers([], 5)

if __name__ == '__main__':
    unittest.main()