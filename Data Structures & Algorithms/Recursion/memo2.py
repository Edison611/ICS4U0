"""
This time we are finding all combinations instead of the least amount of coins.
This can also be similar to the McDonald's chicken nugget problem.
"""

coins = [5, 10, 25]
# coins = [25, 10, 5]
results = []
cache = []


def comb(V):
    print(V)
    """
    Recursive function that gets all combinations of change

    Parameters
    -----------
    V : int
        the value that should be made using the available coins

    Returns
    --------
    str, list
        'IMPOSSIBLE' if the value is unattainable
        list of the combination if value is obtainable
    """
    # Check if case is relevant
    give = [0 for i in range(len(coins))]
    for i in range(len(V)):
        if i == len(V) - 1:
            break

        dif = int(V[i] - V[i + 1])
        ind = coins.index(dif)
        give[ind] = give[ind] + 1
    # print(give)
    if give in cache:
        return V
    cache.append(give)
    # Base case
    if V[-1] == 0:
        results.append(give)
        return V

    result = [-1]

    # Try every coin that has smaller value than V
    for coin in coins:
        if coin > V[-1]:
            continue
        new = list(V)
        new.append(V[-1] - coin)
        # print(new)
        recur = comb(new)
        if recur == "IMPOSSIBLE":
            continue
        # Check if this is the lowest result
        if len(recur) < len(result) and result[0] != -1:
             result = new
    if result == [-1]:
        return "IMPOSSIBLE"
    else:
        return result


value = [int(input("Please enter a value you want: "))]

comb(value)
if len(results) == 0:
    print("No combination can be made")
else:
    print(f"Here are the values we calculated: {results}")
    print(f"Cache list: {cache}")