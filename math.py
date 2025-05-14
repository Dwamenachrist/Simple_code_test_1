def test_add_with_positive_and_negative():
    # Test that add function handles positive and negative numbers correctly
    result = add(5, -3)  
    assert result == 2, f"Expected 5 + (-3) to equal 2, but got {result}"
