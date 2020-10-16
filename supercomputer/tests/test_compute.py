"""Add test cases for the functions in the compute module."""

from supercomputer import compute


def test_identity():
    """Ensure that the identity function returns the same number."""
    number = 10
    assert compute.identity(number) == number


def test_negate():
    """Ensure that the negate function returns the opposite of the number."""
    number = 10
    assert compute.negate(number) == -number


# TODO: Add the test case for the square function


def test_cube():
    """Ensure that the cube function returns the cube of the number."""
    number = 10
    assert compute.cube(number) == number * number * number


def test_power():
    """Ensure that the power function returns the exponentiation with the number."""
    number = 10
    assert compute.power(number) == number ** number


def test_abs_positive():
    """Ensure that the absolute value function returns the positive of a positive number."""
    number = 10
    assert compute.abs(number) == number


def test_abs_negative():
    """Ensure that the absolute value function returns the positive of a negative number."""
    number = -10
    assert compute.abs(number) == -number


def test_square_root_integer():
    """Ensure that the square root function handles integers correctly."""
    number = 9
    assert compute.sqrt(number) == 3


# TODO: Add the test case for the factorial function
