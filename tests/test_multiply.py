# test_multiply.py
import pytest
from multiply import multiply_numbers as multiply

def test_multiply_normal_cases():
    """
    Test multiply function with normal cases.
    """
    assert multiply(2, 3) == 6
    assert multiply(-2, 3) == -6
    assert multiply(2.5, 3.5) == 8.75

def test_multiply_edge_cases():
    """
    Test multiply function with edge cases.
    """
    assert multiply(0, 5) == 0
    assert multiply(float('inf'), 2) == float('inf')

def test_multiply_error_conditions():
    """
    Test multiply function with error conditions.
    """
    with pytest.raises(TypeError):
        multiply('a', 3)
    with pytest.raises(TypeError):
        multiply([1, 2], 3)

@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 6),
    (-2, 3, -6),
    (2.5, 3.5, 8.75),
    (0, 5, 0),
])
def test_multiply_parameterized(a, b, expected):
    """
    Test multiply function with various inputs using parameterization.
    """
    assert multiply(a, b) == expected

@pytest.mark.parametrize("a, b", [
    ('a', 3),
    ([1, 2], 3),
])
def test_multiply_error_conditions_parameterized(a, b):
    """
    Test multiply function with error conditions using parameterization.
    """
    with pytest.raises(TypeError):
        multiply(a, b)