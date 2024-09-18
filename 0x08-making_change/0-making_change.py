#!/usr/bin/python3
"""
This module works out lowest amount of coins needed to
match a total
"""


def makeChange(coins, total):
    """
    Determine fewest number of coins needed to meet given total
    """
    if total <= 0:
        return 0
    
    coins.sort(reverse=True)
    
    lowest_amount_coins = 0
    for coin in coins:
        if total <= 0:
            break
        lowest_amount_coins += total // coin
        total %= coin
    
    if total != 0:
        return -1
    
    return lowest_amount_coins
