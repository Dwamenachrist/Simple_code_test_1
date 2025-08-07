import unittest
from multiply import multiply

class TestMultiply(unittest.TestCase):

    def test_multiply_positive_integers(self):
        self.assertEqual(multiply(3, 5), 15)

    def test_multiply_negative_integers(self):
        self.assertEqual(multiply(-3, -5), 15)

    def test_multiply_positive_and_zero(self):
        self.assertEqual(multiply(0, 5), 0)
        self.assertEqual(multiply(3, 0), 0)

    def test_multiply_negative_and_zero(self):
        self.assertEqual(multiply(0, -5), 0)

    def test_multiply_two_negative_integers(self):
        self.assertEqual(multiply(-3, 5), -15)

    def test_multiply_one(self):
        self.assertEqual(multiply(1, 5), 5)

    def test_multiply_negative_one(self):
        self.assertEqual(multiply(-1, 5), -5)

    def test_multiply_floats(self):
        self.assertAlmostEqual(multiply(2.5, 4), 10.0)
        self.assertAlmostEqual(multiply(-2.5, -4), 10.0)

if __name__ == '__main__':
    unittest.main()