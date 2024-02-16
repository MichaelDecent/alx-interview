#!/usr/bin/python3
"""
This Module contains a function that runs Prime Game
"""
from typing import List, Union


def is_prime(num: int) -> bool:
    """Determines the prime number"""
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def isWinner(x: int, nums: List[int]) -> Union[str, None]:
    """Determines the Winner"""
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if n == 1 or n == 2:
            ben_wins += 1
            continue

        primes = [i for i in range(2, n + 1) if is_prime(i)]

        if len(primes) % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif maria_wins < ben_wins:
        return "Ben"
    else:
        return None
