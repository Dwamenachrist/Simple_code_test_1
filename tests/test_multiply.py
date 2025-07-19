import pytest
from multiply import multiply_numbers

@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 6),                   # Normal case with two positive integers
    (-2, 3, -6),                 # Negative and positive
    (2, -3, -6),                 # Positive and negative
    (-2, -3, 6),                 # Two negatives
    (2.5, 4.0, 10.0),            # Positive float
    (0, 5, 0),                   # Zero multiplication
    (5, 0, 0),                   # Zero multiplication (reverse)
    (1, 5, 5),                   # Multiplying by one
    (5, 1, 5),                   # Multiplying by one (reverse)
    (1e12, 1e12, 1e24),          # Large numbers
    (0.1, 0.2, pytest.approx(0.02, rel=1e-9)),  # Floating point precision
    (2, 2.5, 5.0),               # Mixed types
    (2.5, 2, 5.0)                # Mixed types (reverse)
])
def test_multiply_numbers(a, b, expected):
    """Test multiply_numbers with various inputs."""
    assert multiply_numbers(a, b) == expected

@pytest.mark.parametrize("a, b", [
    ("string", 3),               # Invalid type string
    (None, 3),                   # Invalid type None
    ([], 5),                     # Invalid type list
])
def test_multiply_numbers_invalid_types(a, b):
    """Test multiply_numbers with invalid input types, expecting TypeError."""
    with pytest.raises(TypeError):
        multiply_numbers(a, b)

def test_multiply_numbers_missing_arguments():
    """Test multiply_numbers without arguments, expecting TypeError."""
    with pytest.raises(TypeError):
        multiply_numbers()