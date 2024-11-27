#!/usr/bin/python3
"""Total Count Module"""


def makeChange(coins, total):
    """Return the minimum number of coins to make up the total"""
    if total <= 0:
        return 0

    # Create DP array, initialized to a very large value
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # Base case: 0 coins are needed for total = 0

    # Fill the DP array
    for coin in coins:
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    # If the value at dp[total] is still inf, it means it's impossible
    return dp[total] if dp[total] != float('inf') else -1
