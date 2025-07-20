import pytest
from multiply import multiply_numbers

@pytest.mark.parametrize("a, b, expected", [
    (3, 4, 12),           # Normal case
    (-1, 5, -5),         # Normal case with negative
    (2.5, 4.0, 10.0),    # Normal case with floats
    (0, 5, 0),           # Edge case with zero
    (5, 0, 0),           # Edge case with zero, reversed
    (0, 0, 0),           # Edge case with zero
    (1e20, 1e20, 1e40),  # Edge case with large numbers
    (1e-20, 1e-20, 1e-40) # Edge case with small numbers
])
def test_normal_and_edge_cases(a, b, expected):
    """Test normal and edge cases for multiply_numbers."""
    assert multiply_numbers(a, b) == expected

@pytest.mark.parametrize("a, b", [
    ('a', 5),            # Error case: string
    ([1, 2], 5),        # Error case: list
    (None, 5)           # Error case: NoneType
])
def test_error_cases(a, b):
    """Test error cases for multiply_numbers, expecting TypeError."""
    with pytest.raises(TypeError):
        multiply_numbers(a, b)

def test_boolean_multiplication():
    """Test multiplication with a boolean input."""
    assert multiply_numbers(True, 5) == 5