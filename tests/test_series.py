from math_series.series import fibonacci
from math_series.series import lucas

def test_fibonacci_15():
    expected= [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377]
    actual=fibonacci(15)
    assert expected == actual


def test_fibonacci_7():
    expected=13
    actual=fibonacci(7)
    assert expected == actual


def test_lucas_10():
    expected=123
    actual=lucas(10)
    assert expected == actual