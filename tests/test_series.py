from math_series.series import fibonacci
from math_series.series import lucas
from math_series.series import sum_series

def test_fibonacci_15():
    expected= 610 #[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377]
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

def test_sum_series_as_fib():
    expected = 13
    actual = sum_series(7,0,1)
    assert expected == actual

def test_sum_series_as_luc():
    expected = 123
    actual = sum_series(10,2,1)
    assert expected == actual