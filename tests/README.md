# Unit Tests for Multiply Function

This directory contains the unit tests for the `multiply_numbers` function located in `multiply.py`. The tests are designed to ensure the correctness of the multiplication functionality across various scenarios:

- Testing multiplication of integers (both positive and negative)
- Testing multiplication with zero
- Testing multiplication with floating-point numbers

## Running Tests
To execute the tests, run the following command in the terminal:
```bash
python -m unittest discover -s tests
```

## Expected Outcomes
The tests should pass without errors if the implementation of the multiplication function is correct. In case of failures, investigate the outputs and adjust the `multiply_numbers` function accordingly.

## Future Improvements
Consider extending the test cases to cover edge cases such as:
- Very large integers
- Non-numeric inputs