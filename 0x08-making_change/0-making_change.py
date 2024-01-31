#!/usr/bin/python3
"""
This Module contains a function that determines the
fewest number of coins needed to meet a given amount 
"""


def makeChange(coins, total):
    """determine the fewest number of
    coins needed to meet a given amount
    """
    if total <= 0:
        return 0
    coins.sort(reverse=True)

    count_list = [coins[0]]

    for value in coins:
        current_total = sum(count_list)
        remainder = total % sum(count_list)
        while current_total < total and remainder >= value:
            count_list.append(value)
            current_total = sum(count_list)
            remainder = total % sum(count_list)
            if current_total == total:
                return len(count_list)
            elif current_total > total:
                return -1
    return -1
