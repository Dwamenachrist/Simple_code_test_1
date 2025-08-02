import unittest
from multiply import multiply

class TestMultiply(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(multiply(4, 5), 20)

    def test_negative_numbers(self):
        self.assertEqual(multiply(-2, 3), -6)
        self.assertEqual(multiply(2, -3), -6)
        self.assertEqual(multiply(-2, -3), 6)

    def test_zero(self):
        self.assertEqual(multiply(0, 5), 0)
        self.assertEqual(multiply(5, 0), 0)
        self.assertEqual(multiply(0, 0), 0)

    def test_floats(self):
        self.assertEqual(multiply(2.5, 4), 10.0)
        self.assertEqual(multiply(2, 3.5), 7.0)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            multiply('a', 3)
        with self.assertRaises(TypeError):
            multiply(2, 'b')

if __name__ == '__main__':
    unittest.main()