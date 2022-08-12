import math
from functools import lru_cache


def coinChange(coins, amount):
    @lru_cache(None)
    def cache(amount):
        if amount == 0:
            return 0

        res = math.inf
        for coin in coins:
            if amount >= coin:
                res = min(res, cache(amount - coin) + 1)
        return res

    res = cache(amount)
    return res if res != math.inf else -1


if __name__ == '__main__':
    coins, amount = [1, 2, 5], 11
    print(coinChange(coins, amount))  # 3
    coins, amount = [2], 3
    print(coinChange(coins, amount))  # -1
