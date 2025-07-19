import pytest

def multiply_numbers(a, b):
    return a * b

# Normal test cases
def test_multiply_positive_numbers():
    """Test multiplying two positive integers."""
    assert multiply_numbers(2, 3) == 6

def test_multiply_negative_number():
    """Test multiplying a negative and a positive integer."""
    assert multiply_numbers(-1, 5) == -5

def test_multiply_zero():
    """Test multiplying zero with a positive integer."""
    assert multiply_numbers(0, 10) == 0

def test_multiply_float():
    """Test multiplying a float with an integer."""
    assert multiply_numbers(2.5, 4) == 10.0

def test_multiply_negative_float():
    """Test multiplying a negative float with a positive integer."""
    assert multiply_numbers(-3.5, 2.0) == -7.0

# Edge test cases
def test_multiply_large_numbers():
    """Test multiplying large numbers."""
    assert multiply_numbers(1e10, 2) == 20000000000.0

def test_multiply_negative_large_numbers():
    """Test multiplying two large negative numbers."""
    assert multiply_numbers(-1e10, -1e10) == 1e20

def test_multiply_infinity():
    """Test multiplying infinity with a number."""
    assert multiply_numbers(float('inf'), 2) == float('inf')

def test_multiply_nan():
    """Test multiplying NaN with a number."""
    assert multiply_numbers(float('nan'), 5) != 5  # NaN is not equal to itself

# Error test cases
def test_multiply_string_and_number():
    """Test multiplying a string and a number should raise TypeError."""
    with pytest.raises(TypeError):
        multiply_numbers('a', 3)

def test_multiply_list_and_number():
    """Test multiplying a list and a number should raise TypeError."""
    with pytest.raises(TypeError):
        multiply_numbers([2], 3)

def test_multiply_none_and_number():
    """Test multiplying None and a number should raise TypeError."""
    with pytest.raises(TypeError):
        multiply_numbers(None, 5)