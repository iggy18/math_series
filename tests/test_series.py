from math_series.series import fibonacci, lucas, sum_series

def test_import():
    assert fibonacci

def test_fibonacci_neg():
    actual = fibonacci(-1)
    expected = None
    assert actual == expected

def test_fibonacci_0():
    actual = fibonacci(0)
    expected = 0
    assert actual == expected

def test_fibonacci_1():
    actual = fibonacci(1)
    expected = 1
    assert actual == expected

def test_fibonacci_2():
    actual = fibonacci(2)
    expected = 1
    assert actual == expected

def test_fibonacci_3():
    actual = fibonacci(3)
    expected = 2
    assert actual == expected

def test_fibonacci_4():
    actual = fibonacci(4)
    expected = 3
    assert actual == expected

def test_fibonacci_7():
    actual = fibonacci(7)
    expected = 13
    assert actual == expected

def test_import1():
    assert lucas

def test_lucas_0():
    actual = lucas(0)
    expected = 2
    assert actual == expected

def test_lucas_1():
    actual = lucas(1)
    expected = 1
    assert actual == expected

def test_lucas_2():
    actual = lucas(2)
    expected = 3
    assert actual == expected

def test_lucas_3():
    actual = lucas(3)
    expected = 4
    assert actual == expected

def test_lucas_7():
    actual = lucas(7)
    expected = 29
    assert actual == expected

def test_import2():
    assert sum_series


