#!/usr/bin/python3
"""
This Module contains a function that determines the
fewest number of coins needed to meet a given amount 
"""
def makeChange(coins, total):
    """Determine the fewest number of coins needed to meet a given amount."""
    if total <= 0 or not coins:
        return 0

    coins.sort(reverse=True)
    count_list = []

    for coin in coins:
        while total >= coin:
            count_list.append(coin)
            total -= coin

    if total == 0:
        return len(count_list)
    else:
        return -1
