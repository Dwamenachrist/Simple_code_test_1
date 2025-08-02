import unittest

from multiply import multiply_numbers

class TestMultiplyNumbers(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(multiply_numbers(2, 3), 6)
        self.assertEqual(multiply_numbers(5, 5), 25)

    def test_negative_numbers(self):
        self.assertEqual(multiply_numbers(-1, -1), 1)
        self.assertEqual(multiply_numbers(-1, 2), -2)

    def test_zero(self):
        self.assertEqual(multiply_numbers(0, 5), 0)
        self.assertEqual(multiply_numbers(0, 0), 0)

    def test_floats(self):
        self.assertAlmostEqual(multiply_numbers(2.5, 4), 10.0)
        self.assertAlmostEqual(multiply_numbers(3.1, 2), 6.2)

if __name__ == '__main__':
    unittest.main()