import pytest

def multiply_numbers(a, b):
    """Multiplies two numbers."""
    return a * b

def test_multiply_two_positive_integers():
    """Test multiplying two positive integers."""
    assert multiply_numbers(2, 3) == 6

def test_multiply_two_negative_integers():
    """Test multiplying two negative integers."""
    assert multiply_numbers(-2, -3) == 6

def test_multiply_positive_and_negative_integer():
    """Test multiplying a positive integer by a negative integer."""
    assert multiply_numbers(2, -3) == -6

def test_multiply_by_zero():
    """Test multiplying by zero."""
    assert multiply_numbers(0, 10) == 0

@pytest.mark.parametrize("a, b, expected", [
    (1000000, 2000000, 2000000000000),
    (0.0001, 0.0002, 0.00000002),
    (1000000, 0.0001, 100)
])
def test_edge_cases(a, b, expected):
    """Test edge cases for large and small numbers."""
    assert multiply_numbers(a, b) == expected

@pytest.mark.parametrize("a, b", [
    ("a", 3),
    ([1, 2], 3),
    (2, 3, 4)
])
def test_error_conditions(a, b):
    """Test error conditions with non-numeric inputs."""
    with pytest.raises(TypeError):
        multiply_numbers(a, b)