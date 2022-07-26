import sys


# Time - O(N) | Space - O(1)
def maxProfit(prices):
    profit = 0
    curr = sys.maxsize
    for price in prices:
        curr = min(curr, price)
        profit = max(profit, price - curr)
    return profit


# Time - O(N) | Space - O(1)
def maxProfit(prices):
    maxCur = maxSoFar = 0
    for i in range(1, len(prices)):
        maxCur += prices[i] - prices[i - 1]
        maxCur = max(0, maxCur)
        maxSoFar = max(maxCur, maxSoFar)
    return maxSoFar


if __name__ == '__main__':
    prices1 = [7, 1, 5, 3, 6, 4]
    prices2 = [7, 6, 4, 3, 1]
    print(maxProfit(prices1))  # 5
    print(maxProfit(prices2))  # 0
