# Pull Request: Add Unit Tests for Multiply Numbers Function

## Purpose
The purpose of this pull request is to add comprehensive unit tests for the `multiply_numbers` function in the `multiply.py` module. These tests ensure that the function behaves as expected under various scenarios and edge cases.

## Coverage
The unit tests cover the following scenarios: 
- Positive integer multiplication
- Negative integer multiplication
- Multiplication by zero
- Multiplication of decimal numbers
- Handling of incorrect types (e.g., string inputs)

## Implementation
The tests utilize the `unittest` framework to create a suite of tests for the `multiply_numbers` function. Each method within the `TestMultiplyNumbers` class corresponds to a specific test case.

## Setup
To run the tests, execute the following command in your terminal:
```bash
python -m unittest tests/test_multiply.py
```
Make sure you have Python and the required packages installed.

## Future Work
Future enhancements may include additional tests for edge cases and further validation of input types and behaviors. This could comprise test cases for complex numbers or lists as inputs.