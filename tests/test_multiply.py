import pytest
import multiply

def test_multiply_positive_integers():
    """Test multiplication of two positive integers."""
    assert multiply.multiply_numbers(2, 3) == 6

def test_multiply_negative_and_positive_integers():
    """Test multiplication of a negative integer and a positive integer."""
    assert multiply.multiply_numbers(-2, 3) == -6

def test_multiply_two_negative_integers():
    """Test multiplication of two negative integers."""
    assert multiply.multiply_numbers(-2, -3) == 6

def test_multiply_zero_with_positive_integer():
    """Test multiplication of zero with a positive integer."""
    assert multiply.multiply_numbers(0, 5) == 0

def test_multiply_zero_with_negative_integer():
    """Test multiplication of zero with a negative integer."""
    assert multiply.multiply_numbers(0, -5) == 0

def test_multiply_floating_point_numbers():
    """Test multiplication of two floating point numbers."""
    assert multiply.multiply_numbers(2.5, 2) == 5.0

def test_multiply_with_one():
    """Test multiplication with one as the factor."""
    assert multiply.multiply_numbers(1, 5) == 5

def test_multiply_very_large_integers():
    """Test multiplication of very large integers."""
    assert multiply.multiply_numbers(123456789, 987654321) == 121932631112635269

def test_multiply_very_small_floating_point_numbers():
    """Test multiplication of very small floating point numbers."""
    assert multiply.multiply_numbers(1e-10, 1e-10) == 1e-20

def test_multiply_identity_property():
    """Test multiplication of zero with zero."""
    assert multiply.multiply_numbers(0, 0) == 0

@pytest.mark.parametrize("a, b", [
    ("string", 5),
    ([1, 2], 3),
    ({"key": "value"}, 5),
    (None, 5),
])
def test_multiply_non_numeric_input(a, b):
    """Test multiplication with non-numeric input."""
    with pytest.raises(TypeError):
        multiply.multiply_numbers(a, b)