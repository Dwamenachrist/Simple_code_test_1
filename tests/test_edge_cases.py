import unittest
from multiply import multiply

class TestEdgeCases(unittest.TestCase):

    def test_multiply_large_numbers(self):
        self.assertEqual(multiply(10**6, 10**6), 10**12)

    def test_multiply_non_numeric(self):
        with self.assertRaises(TypeError):
            multiply('string', 5)

    def test_multiply_none(self):
        with self.assertRaises(TypeError):
            multiply(None, 5)

    def test_multiply_boolean(self):
        self.assertEqual(multiply(True, 3), 3)
        self.assertEqual(multiply(False, 3), 0)

if __name__ == '__main__':
    unittest.main()