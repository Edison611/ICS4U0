"""
This solution is a modified one from
https://www.geeksforgeeks.org/find-minimum-number-of-coins-that-make-a-change/
"""

coins = [25, 5, 10]
def minCoins(V):
    # base case
    if V == 0:
        return 0

    # Initialize result
    result = 999999

    # Try every coin that has smaller value than V
    for coin in coins:
        if coin > V:
            continue
        recur = minCoins(V - coin)

        # Check if this is the lowest result
        if recur + 1 < result:
            result = recur + 1
    return result


V = 30
print("Minimum coins required is:", minCoins(V))