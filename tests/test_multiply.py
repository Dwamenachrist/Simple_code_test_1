import pytest
from multiply import multiply_numbers

def test_multiply_positive_numbers():
    assert multiply_numbers(2, 3) == 6

def test_multiply_negative_numbers():
    assert multiply_numbers(-2, -3) == 6

def test_multiply_mixed_signs():
    assert multiply_numbers(-2, 3) == -6

def test_multiply_by_zero():
    assert multiply_numbers(2, 0) == 0

@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 6),
    (-2, -3, 6),
    (-2, 3, -6),
    (2, 0, 0),
])
def test_multiply(a, b, expected):
    assert multiply_numbers(a, b) == expected

def test_multiply_non_numeric_input():
    with pytest.raises(TypeError):
        multiply_numbers("a", 3)

def test_multiply_large_numbers():
    assert multiply_numbers(1000000, 2000000) == 2000000000000

def test_multiply_floats():
    assert multiply_numbers(2.5, 3.5) == 8.75