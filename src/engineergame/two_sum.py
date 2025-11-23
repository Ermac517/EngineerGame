"""Module to find two indices in a list that sum up to a target value."""

def two_sum(nums, target):
    """Find indices of the two numbers that add up to the target.

    Args:
        nums (List[int]): List of integers.
        target (int): Target sum.

    Returns:
        Tuple[int, int]: Indices of the two numbers adding up to target.

    Raises:
        ValueError: If no two numbers sum up to the target.
    """
    num_to_index = {}
    for index, num in enumerate(nums):
        complement = target - num
        if complement in num_to_index:
            return (num_to_index[complement], index)
        num_to_index[num] = index
    raise ValueError("No two sum solution")


def main():
    """Run test cases for two_sum function."""
    test_cases = [
        ([2, 7, 11, 15], 9, (0, 1)),
        ([3, 2, 4], 6, (1, 2)),
        ([3, 3], 6, (0, 1)),
        ([1, 5, 3, 7, 9], 10, (1, 3)),
        ([-1, -2, -3, -4, -5], -8, (2, 4)),
    ]
    
    print("Running two_sum test cases:\n")
    
    for i, (nums, target, expected) in enumerate(test_cases, 1):
        try:
            result = two_sum(nums, target)
            status = "✓ PASS" if result == expected else f"✗ FAIL (expected {expected}, got {result})"
            print(f"Test {i}: nums={nums}, target={target}")
            print(f"  Result: {result} - {status}\n")
        except ValueError as e:
            print(f"Test {i}: nums={nums}, target={target}")
            print(f"  Error: {e}\n")
    
    # Test case that should raise ValueError
    print("Testing error case (no solution):")
    try:
        result = two_sum([1, 2, 3], 10)
        print(f"  ✗ FAIL - Expected ValueError but got {result}\n")
    except ValueError as e:
        print(f"  ✓ PASS - Correctly raised ValueError: {e}\n")


if __name__ == "__main__":
    main()