import pytest
from multiply import multiply_numbers  # Import the function to be tested

def test_multiply_positive_integers():
    """Test multiplication of two positive integers."""
    assert multiply_numbers(3, 4) == 12

def test_multiply_positive_negative_integers():
    """Test multiplication of a positive integer and a negative integer."""
    assert multiply_numbers(5, -2) == -10

def test_multiply_negative_integers():
    """Test multiplication of two negative integers."""
    assert multiply_numbers(-3, -7) == 21

def test_multiply_positive_negative_floats():
    """Test multiplication of a positive float and a negative float."""
    assert multiply_numbers(2.5, -4.2) == -10.5

def test_multiply_large_integers():
    """Test multiplication of two large integers."""
    assert multiply_numbers(1000000000, 2000000000) == 2000000000000000000

def test_multiply_by_zero():
    """Test multiplication involving zero with a positive integer."""
    assert multiply_numbers(0, 5) == 0

def test_multiply_zero_negative():
    """Test multiplication of zero and a negative number."""
    assert multiply_numbers(0, -5) == 0

def test_multiply_large_floats():
    """Test multiplication of two very large floating-point numbers."""
    with pytest.raises(OverflowError):  # Assuming it raises OverflowError on overflow
        multiply_numbers(1.7e+308, 1.7e+308)

def test_multiply_very_small_numbers():
    """Test multiplication of two very small numbers."""
    assert multiply_numbers(1e-10, 1e-10) == 1e-20

def test_multiply_string():
    """Test multiplication where one input is a string."""
    with pytest.raises(TypeError):
        multiply_numbers("string", 4)

def test_multiply_none():
    """Test multiplication where one input is None."""
    with pytest.raises(TypeError):
        multiply_numbers(None, 3)

def test_multiply_two_strings():
    """Test multiplication of two strings."""
    with pytest.raises(TypeError):
        multiply_numbers("three", "four")

def test_multiply_complex():
    """Test multiplication involving a complex number."""
    with pytest.raises(TypeError):  # Assuming it raises TypeError for complex
        multiply_numbers(2 + 3j, 5)