#!/usr/bin/python3
"""determine the fewest number of coins needed to meet a given amount total"""


def makeChange(coins, total):
    """
    Args
       coins - list of coin denominations, number of each denom is unlimited
    Returns
       0  - if total is zero or less
       -1 - if the given coins cannot meet the given total
       1  - if the biggest denomination coin meets the total
       chosenCoinCount - counted coins from coins list that meet the total
    """
    chosenCoinCount = 0
    coins.sort(reverse=True)

    if total <= 0 or any(i == 0 for i in coins):
        return 0

    if coins[0] == total:
        return 1

    if total % coins[0] == 0:
        chosenCoinCount = total // coins[0]
        return chosenCoinCount
    for coin in coins:
        while total >= coin:
            chosenCoinCount += 1
            total -= coin

    if total == 0:
        return chosenCoinCount
    else:
        return -1
