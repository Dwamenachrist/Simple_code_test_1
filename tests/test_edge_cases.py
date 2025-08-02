import unittest
from multiply import multiply

class TestMultiplyEdgeCases(unittest.TestCase):
    def test_edge_cases(self):
        self.assertEqual(multiply(float('inf'), 1), float('inf'))
        self.assertEqual(multiply(1, float('-inf')), float('-inf'))
        self.assertEqual(multiply(float('nan'), 1), float('nan'))
        self.assertEqual(multiply(1, float('nan')), float('nan'))

if __name__ == '__main__':
    unittest.main()