import pytest   # noqa: F401
from dummy_project import methods


def test_add():
    result = methods.add(1, 2)
    assert result == 3


def test_subtract():
    result = methods.subtract(1, 2)
    assert result == -1


def test_multiply():
    result = methods.multiply(1, 2)
    assert result == 2


def test_divide():
    result = methods.divide(1, 2)
    assert result == 0.5
