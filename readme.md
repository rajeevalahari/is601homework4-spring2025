# Project Install Instructions

## install

1. clone
2. pip install -r requirements.txt

## Testing

1. pytest
2. pytest --pylint
3. pytest --pylint --cov

## My Understanding
1. The advanced calculator in part 3 uses static methods on the `Calculator`, instance methods on `Calculation`, and class methods on the `Calculations` class. 
2. It also includes advanced testing with parameterized data and fixtures for consistent test setup.
3. Used faker for parameterized test data.