#!/usr/bin/python3
"""
This module finds the winner of the Prime Game after x rounds
"""


def isWinner(x, nums):
    """
    This function finds winner of Prime Game after x rounds
    """
    if x == 0 or not nums:
        return None

    maximum_num = max(nums)
    sieve = [True] * (maximum_num + 1)
    sieve[0] = sieve[1] = False

    for i in range(2, int(maximum_num ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, maximum_num + 1, i):
                sieve[j] = False

    primes = [i for i in range(2, maximum_num + 1) if sieve[i]]

    def count_moves(n):
        removed = [False] * (n + 1)
        move_count = 0

        for prime in primes:
            if prime > n:
                break
            if not removed[prime]:
                move_count += 1
                for multiple in range(prime, n + 1, prime):
                    removed[multiple] = True
        return move_count

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        moves = count_moves(n)
        if moves % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
