import unittest
import time
from multiply import multiply

class TestPerformance(unittest.TestCase):

    def test_performance_large_numbers(self):
        start_time = time.time()
        result = multiply(10**6, 10**6)
        elapsed_time = time.time() - start_time
        self.assertEqual(result, 10**12)
        self.assertLess(elapsed_time, 1)  # Ensure it runs in less than 1 second

if __name__ == '__main__':
    unittest.main()