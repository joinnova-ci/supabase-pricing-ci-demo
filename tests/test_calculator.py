"""Test suite for calculator functions."""

from calculator import (
    add, subtract, multiply, divide, power,
    modulo, absolute, square_root, factorial, max_of_two
)
import pytest


def test_addition():
    """Test addition function."""
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
    assert add(100, 200) == 300


def test_subtraction():
    """Test subtraction function."""
    assert subtract(5, 3) == 2
    assert subtract(0, 5) == -5
    assert subtract(-3, -3) == 0
    assert subtract(100, 50) == 50


def test_multiplication():
    """Test multiplication function."""
    assert multiply(3, 4) == 12
    assert multiply(0, 5) == 0
    assert multiply(-2, 3) == -6
    assert multiply(7, 1) == 7


def test_division():
    """Test division function."""
    assert divide(10, 2) == 5
    assert divide(7, 2) == 3.5
    assert divide(-10, 2) == -5
    with pytest.raises(ValueError):
        divide(5, 0)


def test_power():
    """Test power function."""
    assert power(2, 3) == 8
    assert power(5, 0) == 1
    assert power(10, 2) == 100
    assert power(3, 3) == 27


def test_modulo():
    """Test modulo function."""
    assert modulo(10, 3) == 1
    assert modulo(20, 5) == 0
    assert modulo(7, 2) == 1
    assert modulo(15, 4) == 3


def test_absolute():
    """Test absolute value function."""
    assert absolute(5) == 5
    assert absolute(-5) == 5
    assert absolute(0) == 0
    assert absolute(-100) == 100


def test_square_root():
    """Test square root function."""
    assert square_root(4) == 2
    assert square_root(9) == 3
    assert square_root(16) == 4
    with pytest.raises(ValueError):
        square_root(-1)


def test_factorial():
    """Test factorial function."""
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(5) == 120
    with pytest.raises(ValueError):
        factorial(-1)


def test_max_of_two():
    """Test max of two numbers function."""
    assert max_of_two(5, 3) == 5
    assert max_of_two(3, 5) == 5
    assert max_of_two(-1, -5) == -1
    assert max_of_two(0, 0) == 0
