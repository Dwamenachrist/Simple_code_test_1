import pytest
from multiply import multiply_numbers as multiply

@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 6),
    (-2, 3, -6),
    (2.5, 3, 7.5),
    (0, 3, 0),
])
def test_multiply_normal_cases(a, b, expected):
    """
    Test multiply function with normal cases.
    """
    assert multiply(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (1e308, 2, pytest.approx(2e308)),
    (1e-323, 2, pytest.approx(2e-323)),
])
def test_multiply_edge_cases(a, b, expected):
    """
    Test multiply function with edge cases.
    """
    assert multiply(a, b) == expected

def test_multiply_error_conditions():
    """
    Test multiply function with error conditions.
    """
    with pytest.raises(TypeError):
        multiply('a', 3)

def test_multiply_missing_inputs():
    """
    Test multiply function with missing inputs.
    """
    with pytest.raises(TypeError):
        multiply(2)