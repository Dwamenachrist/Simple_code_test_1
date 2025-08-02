# Pull Request to Add Unit Tests for multiply_numbers

## Description
This pull request introduces a new test file `test_multiply.py`, which contains comprehensive unit tests for the `multiply_numbers` function. The tests cover various scenarios, including:

- Multiplying positive numbers
- Multiplying negative numbers
- Multiplying a positive and a negative number
- Multiplying by zero
- Multiplying floating-point numbers

These tests aim to ensure the correctness and reliability of the `multiply_numbers` function. After running this test suite, developers can confidently make changes knowing that they will not break existing functionality. 

## Changes Made:
1. Created a new test file named `test_multiply.py`.
2. Added unit tests for different multiplication scenarios.

## Testing Instructions:
To run the tests, use the command:
```bash
python -m unittest test_multiply.py
```