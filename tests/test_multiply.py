import pytest
from multiply import multiply_numbers

def test_multiply_numbers_normal_cases():
    assert multiply_numbers(2, 3) == 6
    assert multiply_numbers(-2, 3) == -6
    assert multiply_numbers(-2, -3) == 6
    assert multiply_numbers(2.5, 3) == 7.5

def test_multiply_numbers_with_zero():
    assert multiply_numbers(0, 3) == 0
    assert multiply_numbers(-2, 0) == 0
    assert multiply_numbers(0, 0) == 0

def test_multiply_numbers_error_handling():
    with pytest.raises(TypeError):
        multiply_numbers("a", 3)
    with pytest.raises(TypeError):
        multiply_numbers(2, "b")
    with pytest.raises(TypeError):
        multiply_numbers("a", "b")