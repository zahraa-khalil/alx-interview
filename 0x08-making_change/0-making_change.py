#!/usr/bin/python3
"""Total Count Module"""


def makeChange(coins, total):
    """Return the minimum number of coins to make up the total"""
    if total <= 0:
        return 0

    # Initialize DP array
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # Base case: 0 coins are needed for total = 0

    # Fill DP table
    for coin in coins:
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    # Check the result
    return dp[total] if dp[total] != float('inf') else -1
