import pytest
from multiply import multiply_numbers as multiply

@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 6),
    (-2, 3, -6),
    (2.5, 3, 7.5),
    (0, 3, 0),
])
def test_multiply_normal_cases(a, b, expected):
    assert multiply(a, b) == expected

@pytest.mark.parametrize("a, b", [
    (1e308, 2),
    (1e-323, 2),
])
def test_multiply_edge_cases(a, b):
    multiply(a, b)

@pytest.mark.parametrize("a, b, expected_exception", [
    ('a', 3, TypeError),
    (None, 3, TypeError),
])
def test_multiply_error_cases(a, b, expected_exception):
    with pytest.raises(expected_exception):
        multiply(a, b)