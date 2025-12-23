def climbStairs(n: int) -> int:
    """Calculate the number of distinct ways to climb to the top of a staircase with n steps.

    Args:
        n: Number of steps in the staircase.
    Returns:
        Number of distinct ways to reach the top.
    """
    if n <= 1:
        return 1

    first, second = 1, 1
    for _ in range(2, n + 1):
        first, second = second, first + second
    return second

def main():
    """Run test cases for climbStairs function."""
    test_cases = [
        (2, 2, "Two steps"),
        (3, 3, "Three steps"),
        (4, 5, "Four steps"),
        (5, 8, "Five steps"),
        (10, 89, "Ten steps"),
        (0, 1, "Zero steps"),
        (1, 1, "One step"),
    ]
    
    print("Running climbStairs test cases:\n")
    
    for i, (n, expected, description) in enumerate(test_cases, 1):
        result = climbStairs(n)
        status = "✓ PASS" if result == expected else f"✗ FAIL (expected {expected}, got {result})"
        print(f"Test {i}: n={n} - {description}")
        print(f"  Result: {result} - {status}\n")

if __name__ == "__main__":
    main()