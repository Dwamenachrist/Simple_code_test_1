import pytest
from multiply import multiply_numbers

def test_multiply_numbers_positive():
    assert multiply_numbers(2, 3) == 6

def test_multiply_numbers_negative():
    assert multiply_numbers(-2, 3) == -6
    assert multiply_numbers(-2, -3) == 6

def test_multiply_numbers_zero():
    assert multiply_numbers(0, 3) == 0
    assert multiply_numbers(-2, 0) == 0

def test_multiply_numbers_large_numbers():
    assert multiply_numbers(2000, 3000) == 6000000

def test_multiply_numbers_non_numeric_input():
    with pytest.raises(TypeError):
        multiply_numbers('a', 3)
    with pytest.raises(TypeError):
        multiply_numbers(2, 'b')