import unittest
from multiply import multiply_numbers

class TestMultiplyNumbers(unittest.TestCase):

    def test_multiply_integers(self):
        self.assertEqual(multiply_numbers(3, 4), 12)
        self.assertEqual(multiply_numbers(-3, 5), -15)

    def test_multiply_zero(self):
        self.assertEqual(multiply_numbers(0, 10), 0)
        self.assertEqual(multiply_numbers(-2, 0), 0)

    def test_multiply_floats(self):
        self.assertAlmostEqual(multiply_numbers(1.5, 2.0), 3.0)
        self.assertAlmostEqual(multiply_numbers(-1.5, 2.0), -3.0)

if __name__ == '__main__':
    unittest.main()