import pytest
from multiply import multiply_numbers

# Normal Cases
def test_basic_multiplication():
    """Test basic multiplication of two integers."""
    assert multiply_numbers(2, 3) == 6

def test_multiplication_with_float():
    """Test multiplication of an integer and a float."""
    assert multiply_numbers(2.5, 4) == 10.0

def test_multiplication_of_two_floats():
    """Test multiplication of two floats."""
    assert multiply_numbers(1.5, 2.5) == 3.75

def test_multiplication_with_negative_numbers():
    """Test multiplication with one negative and one positive number."""
    assert multiply_numbers(-3, 4) == -12

def test_multiplication_with_zero():
    """Test multiplication with zero."""
    assert multiply_numbers(0, 5) == 0

# Edge Cases
def test_large_numbers():
    """Test multiplication of very large numbers."""
    assert multiply_numbers(1e+15, 1e+15) == 1e+30

def test_small_numbers():
    """Test multiplication of very small numbers (close to zero)."""
    assert multiply_numbers(1e-15, 1e-15) == 1e-30

def test_multiplication_of_one():
    """Test multiplication where one multiplicand is one."""
    assert multiply_numbers(1, 100) == 100

# Error Cases
def test_string_input():
    """Test multiplication with a string as input."""
    with pytest.raises(TypeError):
        multiply_numbers('2', 3)

def test_none_input():
    """Test multiplication with None as input."""
    with pytest.raises(TypeError):
        multiply_numbers(None, 3)

def test_list_input():
    """Test multiplication with a list as input."""
    with pytest.raises(TypeError):
        multiply_numbers([1, 2], 3)

def test_both_strings_input():
    """Test multiplication where both inputs are strings."""
    with pytest.raises(TypeError):
        multiply_numbers('hello', 'world')