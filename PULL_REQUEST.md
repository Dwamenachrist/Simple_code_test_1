# Pull Request for Adding Tests

## Purpose:
This pull request adds new tests for the multiplication functionality in the `tests/test_multiply.py` file. These tests are meant to ensure the correctness of the multiply function under various conditions.

## Coverage:
The following components are now tested:
- Basic multiplication cases
- Edge cases for zero and negative multipliers
- Invalid input handling

## Implementation:
The tests utilize the `unittest` framework and include several test cases to cover the various scenarios outlined above. Each test checks for both correct outputs and proper error handling.

## Setup:
To run the tests, ensure you have Python installed along with the `unittest` package. Execute the command:
```bash
python -m unittest tests/test_multiply.py
```

## Future Work:
Additional tests could be added to handle floating-point arithmetic and performance testing with large numbers.