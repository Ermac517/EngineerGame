import pytest

from engineergame import is_prime, factorial, fibonacci, gcd


def test_is_prime():
    assert not is_prime(0)
    assert not is_prime(1)
    assert is_prime(2)
    assert is_prime(3)
    assert is_prime(13)
    assert not is_prime(15)


def test_factorial():
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(5) == 120
    with pytest.raises(ValueError):
        factorial(-1)


def test_fibonacci():
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(5) == 5
    with pytest.raises(ValueError):
        fibonacci(-3)


def test_gcd():
    assert gcd(0, 5) == 5
    assert gcd(48, 18) == 6
    assert gcd(-48, -18) == 6
