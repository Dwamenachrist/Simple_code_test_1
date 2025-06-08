import pytest
from multiply import multiply_numbers

@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 6),
    (-2, 3, -6),
    (0, 3, 0),
    (2, -3, -6),
    (-2, -3, 6),
    (2.5, 3, 7.5),
    (2, 3.5, 7.0),
    (1e10, 2, 2e10),
    (float('inf'), 2, float('inf')),
])
def test_multiply_numbers_valid_inputs(a, b, expected):
    assert multiply_numbers(a, b) == expected

@pytest.mark.parametrize("a, b, error", [
    ('a', 3, TypeError),
    (2, 'b', TypeError),
    (None, 3, TypeError),
    (2, None, TypeError),
    ([1, 2], 3, TypeError),
    (2, {'a': 1}, TypeError),
])
def test_multiply_numbers_invalid_inputs(a, b, error):
    with pytest.raises(error):
        multiply_numbers(a, b)