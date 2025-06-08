import pytest
from multiply import multiply_numbers as multiply

@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 6),
    (-2, -3, 6),
    (-2, 3, -6),
    (2.5, 3.5, 8.75),
    (0, 3, 0),
    (2, 0, 0),
    (0, 0, 0),
])
def test_multiply_normal_and_edge_cases(a, b, expected):
    """
    Test the multiply function with normal and edge cases.
    
    Parameters:
    a (int/float): The first number to multiply.
    b (int/float): The second number to multiply.
    expected (int/float): The expected product of a and b.
    """
    assert multiply(a, b) == expected

@pytest.mark.parametrize("a, b, error_type", [
    ('a', 3, TypeError),
    (2, 'b', TypeError),
    ([1, 2], 3, TypeError),
])
def test_multiply_error_conditions(a, b, error_type):
    """
    Test the multiply function with error conditions.
    
    Parameters:
    a (any): The first input to test for error.
    b (any): The second input to test for error.
    error_type (Exception): The type of exception expected to be raised.
    """
    with pytest.raises(error_type):
        multiply(a, b)