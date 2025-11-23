"""Module to perform binary search on a sorted list."""
def binary_search(nums, target):
    """Perform binary search to find the index of target in arr.

    Args:
        nums (List[int]): Sorted list of integers.
        target (int): Target value to search for.
    Returns:
        int: Index of target in nums if found, else -1.
    """
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def main():
    """Run test cases for binary_search function."""
    test_cases = [
        ([1, 2, 3, 4, 5], 3, 2),
        ([10, 20, 30, 40, 50], 10, 0),
        ([5, 15, 25, 35, 45], 45, 4),
        ([2, 4, 6, 8, 10], 7, -1),
        ([], 1, -1),
    ]
    
    print("Running binary_search test cases:\n")
    
    for i, (nums, target, expected) in enumerate(test_cases, 1):
        result = binary_search(nums, target)
        status = "✓ PASS" if result == expected else f"✗ FAIL (expected {expected}, got {result})"
        print(f"Test {i}: nums={nums}, target={target}")
        print(f"  Result: {result} - {status}\n")

if __name__ == "__main__":
    main()