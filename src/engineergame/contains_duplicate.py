
from typing import List

def containsDuplicate(nums: List[int]) -> bool:
    """Check if the list contains any duplicates.

    Args:
        nums: List of integers.
    Returns:
        True if any value appears at least twice in the list, False otherwise.
    """   
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False

def main():
    """Run test cases for containsDuplicate function."""
    test_cases = [
        ([1, 2, 3, 1], True, "Contains duplicates"),
        ([1, 2, 3, 4], False, "No duplicates"),
        ([1, 1, 1, 1], True, "All elements are duplicates"),
        ([], False, "Empty list"),
        ([0], False, "Single element list"),
        ([-1, -2, -3, -1], True, "Negative numbers with duplicates"),
    ]
    
    print("Running containsDuplicate test cases:\n")
    
    for i, (nums, expected, description) in enumerate(test_cases, 1):
        result = containsDuplicate(nums)
        status = "✓ PASS" if result == expected else f"✗ FAIL (expected {expected}, got {result})"
        print(f"Test {i}: nums={nums} - {description}")
        print(f"  Result: {result} - {status}\n")


if __name__ == "__main__":
    main()