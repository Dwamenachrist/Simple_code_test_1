import pytest
from multiply import multiply_numbers

# Normal Cases
def test_multiply_two_positive_integers():
    """Test multiplying two positive integers."""
    assert multiply_numbers(3, 4) == 12

def test_multiply_two_negative_integers():
    """Test multiplying two negative integers."""
    assert multiply_numbers(-3, -4) == 12

def test_multiply_positive_and_negative_integers():
    """Test multiplying a positive integer and a negative integer."""
    assert multiply_numbers(3, -4) == -12

def test_multiply_two_floating_point_numbers():
    """Test multiplying two floating-point numbers."""
    assert multiply_numbers(2.5, 4.0) == 10.0

def test_multiply_integer_and_floating_point():
    """Test multiplying an integer and a floating-point number."""
    assert multiply_numbers(3, 2.5) == 7.5

# Edge Cases
def test_multiply_by_zero():
    """Test multiplying by zero."""
    assert multiply_numbers(0, 5) == 0

def test_multiply_two_zeros():
    """Test multiplying two zeros."""
    assert multiply_numbers(0, 0) == 0

def test_multiply_one_with_number():
    """Test multiplying one with another number."""
    assert multiply_numbers(1, 5) == 5

def test_multiply_large_numbers():
    """Test multiplying two very large numbers."""
    assert multiply_numbers(1e10, 1e10) == 1e20

# Error Conditions
def test_multiply_with_string():
    """Test multiplying with a string instead of a number."""
    with pytest.raises(TypeError):
        multiply_numbers('a', 3)

def test_multiply_with_none():
    """Test multiplying with None as an argument."""
    with pytest.raises(TypeError):
        multiply_numbers(None, 5)

def test_multiply_with_multiple_arguments():
    """Test multiplying with more than two arguments."""
    with pytest.raises(TypeError):
        multiply_numbers(2, 3, 4)