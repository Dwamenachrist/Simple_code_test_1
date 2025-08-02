def test_multiply_numbers():
    assert multiply(0, 1) == 0, "Test case 1 failed"
    assert multiply(1, 1) == 1, "Test case 2 failed"
    assert multiply(2, 3) == 6, "Test case 3 failed"
    assert multiply(-1, 1) == -1, "Test case 4 failed"
    assert multiply(-1, -1) == 1, "Test case 5 failed"
    assert multiply(0, 0) == 0, "Test case 6 failed"
    assert multiply(5, 5) == 25, "Test case 7 failed"
    print("All test cases passed")