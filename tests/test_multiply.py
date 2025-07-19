import pytest
from multiply import multiply_numbers

def test_multiply_by_zero():
    """Test that multiplying any number by zero results in zero."""
    assert multiply_numbers(0, 5) == 0
    assert multiply_numbers(5, 0) == 0

def test_multiply_negative_numbers():
    """Test that multiplying two negative numbers results in a positive number."""
    assert multiply_numbers(-5, -10) == 50
    """Test that multiplying a negative and a positive number results in a negative number."""
    assert multiply_numbers(-5, 10) == -50

def test_large_values():
    """Test that multiplying large integers results in the correct product."""
    assert multiply_numbers(10**10, 10**10) == 10**20

def test_decimal_multiply():
    """Test that multiplying floats returns the correct product."""
    assert multiply_numbers(2.5, 4) == 10.0

def test_invalid_input():
    """Test that calling multiply_numbers with non-numeric types raises TypeError."""
    with pytest.raises(TypeError):
        multiply_numbers("a", 5)
    with pytest.raises(TypeError):
        multiply_numbers(5, "b")
    with pytest.raises(TypeError):
        multiply_numbers(None, 5)

# Run the tests
if __name__ == "__main__":
    pytest.main()