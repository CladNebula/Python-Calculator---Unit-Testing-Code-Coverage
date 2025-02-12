"""
Comprehensive unit tests for the calculator module using pytest.

Covers addition, subtraction, multiplication, and division functions,
including edge cases and exceptions.
"""

import pytest
from calculator import add, subtract, multiply, divide

# ---------------- TEST CASES FOR ADDITION ---------------- #
@pytest.mark.parametrize(
    "a, b, expected",
    [
        (2, 3, 5),  # Basic addition
        (-1, 1, 0),  # Positive + Negative
        (0, 0, 0),  # Zero addition
        (1.5, 2.5, 4.0),  # Floating point addition
        (1e10, 1e10, 2e10),  # Large number addition
        (-1e10, 1e10, 0),  # Large positive + Large negative
    ],
)
def test_add(a, b, expected):
    """Tests addition with various cases."""
    assert add(a, b) == expected

# ---------------- TEST CASES FOR SUBTRACTION ---------------- #
@pytest.mark.parametrize(
    "a, b, expected",
    [
        (5, 3, 2),  # Basic subtraction
        (10, 15, -5),  # Resulting in negative
        (0, 0, 0),  # Zero subtraction
        (1.5, 0.5, 1.0),  # Floating point subtraction
        (-10, -5, -5),  # Negative number subtraction
        (1e10, 1e9, 9e9),  # Large numbers
    ],
)
def test_subtract(a, b, expected):
    """Tests subtraction with various cases."""
    assert subtract(a, b) == expected

# ---------------- TEST CASES FOR MULTIPLICATION ---------------- #
@pytest.mark.parametrize(
    "a, b, expected",
    [
        (4, 3, 12),  # Basic multiplication
        (-2, 3, -6),  # Negative times positive
        (0, 10, 0),  # Multiplication with zero
        (1.5, 2, 3.0),  # Floating point multiplication
        (-1, -1, 1),  # Negative times negative
        (1e5, 1e5, 1e10),  # Large number multiplication
    ],
)
def test_multiply(a, b, expected):
    """Tests multiplication with various cases."""
    assert multiply(a, b) == expected

# ---------------- TEST CASES FOR DIVISION ---------------- #
@pytest.mark.parametrize(
    "a, b, expected",
    [
        (6, 2, 3),  # Basic division
        (9, 3, 3),  # Even division
        (5, 2, 2.5),  # Floating point result
        (-10, 2, -5),  # Negative divided by positive
        (-10, -2, 5),  # Negative divided by negative
        (1, 3, 1/3),  # Fractional result
        (1e10, 1e5, 1e5),  # Large number division
    ],
)
def test_divide(a, b, expected):
    """Tests division with various cases."""
    assert divide(a, b) == expected

def test_divide_by_zero():
    """Tests division by zero handling."""
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(10, 0)
