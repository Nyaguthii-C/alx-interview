#!/usr/bin/python3
"""A function to determine winner of Prime game"""


def isPrime(num):
    """Check if a number is prime"""
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def isWinner(x, nums):
    """
    Determines the winner of a prime game.

    Args:
        x (int): The number of rounds.
        nums (list): An array of n for each round.

    Returns:
        str: The name of the player that won the most rounds.
             If the winner cannot be determined, returns None.
    """
    if nums == [] or x == 0:
        # Winner cannot be determined
        return None

    maria_wins = 0
    ben_wins = 0

    for turn in range(x):
        n = nums[turn]
        working_set = set(range(1, n + 1))

        while working_set:
            # Maria's turn
            primes = [i for i in working_set if isPrime(i)]
            if not primes:
                ben_wins += 1
                break
            prime = min(primes)
            #  Remove all multiples of prime from the working set
            working_set -= set(range(prime, n + 1, prime))

            # Ben's turn
            primes = [i for i in working_set if isPrime(i)]
            if not primes:
                maria_wins += 1
                break
            prime = min(primes)
            working_set -= set(range(prime, n + 1, prime))

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
