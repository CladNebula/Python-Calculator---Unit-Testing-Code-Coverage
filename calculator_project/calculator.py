"""
A simple calculator module with basic arithmetic operations.

This module provides functions for addition, subtraction, multiplication,
and division. It also includes logging to track operations and errors.

Author: [Your Name]
Date: [Today's Date]
"""

import logging

# Configure logging
logging.basicConfig(
    filename="calculator.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def add(a: float, b: float) -> float:
    """Returns the sum of two numbers."""
    result = a + b
    logging.info("Adding %s + %s = %s", a, b, result)
    return result

def subtract(a: float, b: float) -> float:
    """Returns the difference of two numbers."""
    result = a - b
    logging.info("Subtracting %s - %s = %s", a, b, result)
    return result

def multiply(a: float, b: float) -> float:
    """Returns the product of two numbers."""
    result = a * b
    logging.info("Multiplying %s * %s = %s", a, b, result)
    return result

def divide(a: float, b: float) -> float:
    """
    Returns the quotient of two numbers.

    Raises:
        ValueError: If division by zero is attempted.
    """
    if b == 0:
        logging.error("Division by zero attempted: %s / %s", a, b)
        raise ValueError("Cannot divide by zero")
    
    result = a / b
    logging.info("Dividing %s / %s = %s", a, b, result)
    return result
