import pytest
from multiply import multiply_numbers

@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 6),
    (-1, 5, -5),
    (0, 5, 0),
    (2.5, 4, 10.0),
    (-2.5, -4, 10.0)
])
def test_multiply_normal_cases(a, b, expected):
    """Test normal cases for multiply_numbers."""
    assert multiply_numbers(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (1e308, 1e308, float('inf')),
    (-1e308, -1e308, float('inf')),
    (0, 1e-10, 0),
    (1e-10, 1e10, 0.1),
    (float('inf'), 10, float('inf'))
])
def test_multiply_edge_cases(a, b, expected):
    """Test edge cases for multiply_numbers."""
    assert multiply_numbers(a, b) == expected

@pytest.mark.parametrize("a, b", [
    ('a', 5),
    (5, None),
    ([2], 3),
    (2, '2'),
    (float('nan'), 5)
])
def test_multiply_error_cases(a, b):
    """Test error cases for multiply_numbers."""
    if isinstance(a, float) and (a != a):  # Check for NaN
        assert multiply_numbers(a, b) != multiply_numbers(a, b)  # NaN case
    else:
        with pytest.raises(TypeError):
            multiply_numbers(a, b)