#!/usr/bin/python3
"""Module for Prime Game"""


def isWinner(x, nums):
    """who wins the game"""
    def sieve_of_eratosthenes(limit):
        primes = [True] * (limit + 1)
        primes[0] = primes[1] = False
        for i in range(2, int(limit ** 0.5) + 1):
            if primes[i]:
                for j in range(i * i, limit + 1, i):
                    primes[j] = False
        return [i for i in range(2, limit + 1) if primes[i]]

    def simulate_game(n):
        # Generate primes up to n
        primes = sieve_of_eratosthenes(n)
        # True means the number is still available
        available_numbers = [True] * (n + 1)
        turns = 0  # Track whose turn it is (0 for Maria, 1 for Ben)

        while primes:
            # The player picks the smallest available prime
            prime = primes.pop(0)
            if not available_numbers[prime]:
                continue
            # Remove the prime and its multiples from the set
            for multiple in range(prime, n + 1, prime):
                available_numbers[multiple] = False
            turns += 1

        # If turns is odd, Maria wins, else Ben wins
        return "Maria" if turns % 2 == 1 else "Ben"

    maria_wins = 0
    ben_wins = 0

    # Simulate each round
    for n in nums:
        winner = simulate_game(n)
        if winner == "Maria":
            maria_wins += 1
        else:
            ben_wins += 1

    # Return the player who won the most rounds
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
