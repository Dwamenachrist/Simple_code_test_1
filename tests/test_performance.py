import time
from multiply import multiply_numbers

def test_performance():
    start_time = time.time()
    multiply_numbers(1000000, 1000000)
    duration = time.time() - start_time
    assert duration < 1, "Performance test failed: took too long"

if __name__ == '__main__':
    test_performance()