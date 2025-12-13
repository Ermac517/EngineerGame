from typing import List


def maxProfit(prices: List[int]) -> int:
    """Calculate the maximum profit from stock prices.

    Args:
        prices (List[int]): List of stock prices where prices[i] is the price on day i.
    Returns:
        int: Maximum profit achievable.
    """
    if not prices:
        return 0

    min_price = prices[0]
    max_profit = 0

    for price in prices:
        if price < min_price:
            min_price = price
        elif price - min_price > max_profit:
            max_profit = price - min_price

    return max_profit


def main():
    """Run test cases for maxProfit function."""
    test_cases = [
        ([7, 1, 5, 3, 6, 4], 5, "Buy at 1, sell at 6"),
        ([7, 6, 4, 3, 1], 0, "Prices only decrease, no profit"),
        ([1, 2, 3, 4, 5], 4, "Prices increase continuously, buy at 1, sell at 5"),
        ([2, 4, 1], 2, "Buy at 2, sell at 4"),
        ([3, 2, 6, 5, 0, 3], 4, "Buy at 2, sell at 6"),
        ([], 0, "Empty prices list"),
        ([5], 0, "Single price, no transaction possible"),
        ([2, 1, 2, 1, 0, 1, 2], 2, "Buy at 0, sell at 2"),
    ]
    
    print("Running maxProfit test cases:\n")
    
    for i, (prices, expected, description) in enumerate(test_cases, 1):
        result = maxProfit(prices)
        status = "✓ PASS" if result == expected else f"✗ FAIL (expected {expected}, got {result})"
        print(f"Test {i}: {description}")
        print(f"  Prices: {prices}")
        print(f"  Result: {result} - {status}\n")


if __name__ == "__main__":
    main()