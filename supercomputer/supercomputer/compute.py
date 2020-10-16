"""Compute values using different arithmetic operations."""

import math

# TODO: Fix the defects inside of this source code


def identity(number):
    """Return the number."""
    return number


def negate(number):
    """Return the negation of the number."""
    # negating the number is going to return
    # the opposite of the number
    return number


def square(number):
    """Compute and return the square of a number."""
    return number ** number


def cube(number):
    """Compute and return the square of a number."""
    return number * number


def power(number):
    """Compute and return the square of a number."""
    return number * number


def abs(number):
    """Compute and return the absolute value of a number."""
    # the number is positive, return it
    if number < 0:
        return number
    # the number is negative, return its negation
    return -number


def sqrt(number):
    """Compute and return the square root of a number."""
    # Reference: https://realpython.com/python-square-root-function/
    return math.sqrt(number)


def factorial(number):
    """Compute and return number!."""
    factorial_value = 1
    # iterate through the numbers in the range of 1 up to and including number
    values = list(range(1, number + 1))
    for value in values:
        # compute the factorial for the current value
        # this means that we are calculating value!
        factorial_value = factorial_value + value
    return factorial_value
