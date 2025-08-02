def multiply(a, b):
    return a * b

def test_multiply():
    assert multiply(1, 1) == 1
    assert multiply(2, 3) == 6
    assert multiply(-1, -1) == 1
    assert multiply(-1, 1) == -1
    assert multiply(0, 10) == 0
    print("All test cases passed")