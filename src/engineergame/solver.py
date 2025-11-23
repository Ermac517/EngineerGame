"""Basic problem-solving utilities.

Functions:
- is_prime(n)
- factorial(n)
- fibonacci(n)
- gcd(a, b)
"""
from typing import Iterator

def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

def factorial(n: int) -> int:
    if n < 0:
        raise ValueError("factorial() not defined for negative values")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def fibonacci(n: int) -> int:
    if n < 0:
        raise ValueError("fibonacci() not defined for negative values")
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

def gcd(a: int, b: int) -> int:
    a, b = abs(a), abs(b)
    if a == 0:
        return b
    if b == 0:
        return a
    while b:
        a, b = b, a % b
    return a
