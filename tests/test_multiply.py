# tests/test_multiply.py
import pytest
from multiply import multiply_numbers as multiply

@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 6),
    (-2, -3, 6),
    (2, -3, -6),
    (2.5, 3.5, 8.75),
])
def test_multiply_normal_cases(a, b, expected):
    """
    Test multiply function with normal cases.
    
    Parameters:
    a (int/float): The first number.
    b (int/float): The second number.
    expected (int/float): The expected result of a * b.
    """
    assert multiply(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (0, 5, 0),
    (5, 0, 0),
    (1000000, 2000000, 2000000000000),
])
def test_multiply_edge_cases(a, b, expected):
    """
    Test multiply function with edge cases.
    
    Parameters:
    a (int/float): The first number.
    b (int/float): The second number.
    expected (int/float): The expected result of a * b.
    """
    assert multiply(a, b) == expected

@pytest.mark.parametrize("a, b, error_type", [
    ('a', 3, TypeError),
    ([1,2], 3, TypeError),
])
def test_multiply_error_conditions_non_numeric(a, b, error_type):
    """
    Test multiply function with non-numeric inputs.
    
    Parameters:
    a (non-numeric): The first non-numeric input.
    b (int/float): The second number.
    error_type (Exception): The expected exception type.
    """
    with pytest.raises(error_type):
        multiply(a, b)

def test_multiply_error_conditions_missing_arguments():
    """
    Test multiply function with missing arguments.
    """
    with pytest.raises(TypeError):
        multiply(2)
    with pytest.raises(TypeError):
        multiply()