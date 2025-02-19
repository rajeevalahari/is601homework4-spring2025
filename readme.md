# Project Install Instructions

## install

1. clone
2. pip install -r requirements.txt

## Testing

1. pytest
2. pytest --pylint
3. pytest --pylint --cov
4. python main.py 2 2 add
5. pytest test/test_main.py

## My Understanding
1. In this homework, I integrated the Faker library to dynamically generate test data for the calculator operations. 
2. I implemented a feature using `pytest` to generate a customizable number of test records, and added exception handling to manage invalid inputs and operations. This approach improved the testing process and allowed for more robust input validation.