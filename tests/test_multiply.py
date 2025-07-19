import pytest
from multiply import multiply_numbers

def test_multiply_positive_integers():
    assert multiply_numbers(3, 5) == 15

def test_multiply_positive_negative():
    assert multiply_numbers(4, -2) == -8

def test_multiply_negative_integers():
    assert multiply_numbers(-3, -7) == 21

def test_multiply_by_zero():
    assert multiply_numbers(0, 5) == 0

def test_multiply_by_one():
    assert multiply_numbers(1, 100) == 100

def test_multiply_large_numbers():
    assert multiply_numbers(1000000, 1000000) == 1000000000000

def test_multiply_negative_with_zero():
    assert multiply_numbers(-10, 0) == 0

def test_multiply_non_numeric_string():
    with pytest.raises(TypeError):
        multiply_numbers('text', 5)

def test_multiply_non_numeric_list():
    with pytest.raises(TypeError):
        multiply_numbers([2], 3)