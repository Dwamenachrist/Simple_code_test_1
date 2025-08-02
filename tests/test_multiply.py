import unittest

from multiply import multiply_numbers

class TestMultiplyNumbers(unittest.TestCase):
    def test_multiply_positive(self):
        self.assertEqual(multiply_numbers(2, 3), 6)

    def test_multiply_negative(self):
        self.assertEqual(multiply_numbers(-1, 10), -10)

    def test_multiply_zero(self):
        self.assertEqual(multiply_numbers(0, 5), 0)

    def test_multiply_float(self):
        self.assertAlmostEqual(multiply_numbers(2.5, 4), 10.0)

    def test_multiply_string(self):
        with self.assertRaises(TypeError):
            multiply_numbers('a', 2)

if __name__ == '__main__':
    unittest.main()