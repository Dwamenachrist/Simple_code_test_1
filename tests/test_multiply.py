import pytest
from multiply import multiply, validate_input

@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 6),
    (-4, 5, -20),
    (3, -7, -21),
    (-2, -5, 10),
    (0, 5, 0),
    (5, 0, 0),
    (0, 0, 0),
    (2.5, 4, 10.0),
    (3, 2.5, 7.5),
    (1e10, 1e10, 1e20)
])
def test_valid_multiplication(a, b, expected):
    """Test valid multiplication cases."""
    assert multiply(a, b) == expected

@pytest.mark.parametrize("a, b", [
    ('a', 3),
    (None, 3),
    ([], 5),
    ({}, 5),
    (True, 5)
])
def test_non_numeric_input(a, b):
    """Test that non-numeric input raises a TypeError."""
    with pytest.raises(TypeError):
        multiply(a, b)

def test_validate_input():
    """Test input validation logic."""
    assert validate_input(2, 3) is True
    assert validate_input(-1.5, 4.2) is True
    with pytest.raises(TypeError):
        validate_input('a', 1)
    with pytest.raises(TypeError):
        validate_input(None, 1)
    with pytest.raises(TypeError):
        validate_input(1, 'b')

@pytest.mark.parametrize("a, b, expected", [
    (2.5, 4.0, 10.0),
    (3.0, 2.5, 7.5),
    (1.0, -1.0, -1.0),
    (-1.0, -1.0, 1.0)
])
def test_decimal_multiplication(a, b, expected):
    """Test multiplication with decimal numbers."""
    assert multiply(a, b) == expected