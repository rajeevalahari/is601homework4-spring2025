"""Pytest configuration file for generating test data dynamically."""

from decimal import Decimal  # Standard library first
from faker import Faker
from calculator.operations import add, subtract, multiply, divide

# Initialize Faker instance
fake = Faker()

def generate_test_data(num_records):
    """Generates test data for calculator operations.

    Args:
        num_records (int): The number of test records to generate.

    Yields:
        tuple: (a, b, operation_name, operation_func, expected_result)
    """
    operation_mappings = {
        'add': add,
        'subtract': subtract,
        'multiply': multiply,
        'divide': divide
    }

    for _ in range(num_records):
        a = Decimal(fake.random_int(min=1, max=99))  # Using random_int for better control
        b = Decimal(fake.random_int(min=1, max=99)) if _ % 4 != 3 else Decimal(fake.random_int(min=1, max=9))
        operation_name = fake.random_element(elements=list(operation_mappings.keys()))
        operation_func = operation_mappings[operation_name]

        # Avoid division by zero
        if operation_func is divide and b == Decimal('0'):
            b = Decimal('1')

        try:
            expected = operation_func(a, b) if operation_func is not divide or b != Decimal('0') else "ZeroDivisionError"
        except ZeroDivisionError:
            expected = "ZeroDivisionError"

        yield a, b, operation_name, operation_func, expected

def pytest_addoption(parser):
    """Adds a command-line option to specify the number of test records."""
    parser.addoption(
        "--num_records",
        action="store",
        default=5,
        type=int,
        help="Number of test records to generate"
    )

def pytest_generate_tests(metafunc):
    """Dynamically generates test cases based on the requested parameters.

    Args:
        metafunc (Metafunc): Pytest metafunc object to inject parameters.
    """
    if {"a", "b", "expected"}.intersection(set(metafunc.fixturenames)):
        num_records = metafunc.config.getoption("num_records")
        parameters = list(generate_test_data(num_records))

        modified_parameters = [
            (a, b, op_name if 'operation_name' in metafunc.fixturenames else op_func, expected)
            for a, b, op_name, op_func, expected in parameters
        ]

        metafunc.parametrize("a,b,operation,expected", modified_parameters)
