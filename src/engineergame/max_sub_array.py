from typing import List

def maxSubArray(nums: List[int]) -> int:
    """Find the contiguous subarray with the largest sum.

    Args:
        nums: List of integers.
    Returns:
        The largest sum of a contiguous subarray.
    """
    max_current = max_global = nums[0]
    
    for num in nums[1:]:
        max_current = max(num, max_current + num)
        if max_current > max_global:
            max_global = max_current
            
    return max_global

def main():
    """Run test cases for maxSubArray function."""
    test_cases = [
        ([-2,1,-3,4,-1,2,1,-5,4], 6, "Example case 1"),
        ([1], 1, "Single positive element"),
        ([5,4,-1,7,8], 23, "Example case 2"),
        ([-1,-2,-3,-4], -1, "All negative elements"),
        ([0,0,0,0], 0, "All zeros"),
        ([2,-1,2,3,4,-5], 10, "Mixed elements"),
    ]
    
    print("Running maxSubArray test cases:\n")
    
    for i, (nums, expected, description) in enumerate(test_cases, 1):
        result = maxSubArray(nums)
        status = "✓ PASS" if result == expected else f"✗ FAIL (expected {expected}, got {result})"
        print(f"Test {i}: nums={nums} - {description}")
        print(f"  Result: {result} - {status}\n")

if __name__ == "__main__":
    main()