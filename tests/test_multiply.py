import pytest
from multiply import multiply

def test_multiply_basic():
    assert multiply(2, 3) == 6
    assert multiply(-1, 1) == -1
    assert multiply(0, 10) == 0


def test_multiply_performance():
    import time
    start_time = time.time()
    result = multiply(1000000, 1000000)
    end_time = time.time()
    assert result == 1000000000000
    assert end_time - start_time < 1  # Should take less than 1 second


def test_multiply_edge_cases():
    assert multiply(1, 0) == 0
    assert multiply(0, 0) == 0
    assert multiply(1.5, 2) == 3.0
    assert multiply(-1, -1) == 1