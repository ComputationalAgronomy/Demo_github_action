import pytest

from a1_q1 import a1_q1


def test_q1_t1():
    result = a1_q1(100, degree="F")
    expected = 212
    assert result == expected


def test_a1_t2():
    result = a1_q1(32, degree="C")
    expected = 0
    assert result == expected
