# -----------------------------------------------------------------------------
# Name:        Recursion Assignment
# Purpose:     To create a recursion program using a recursive method to solve problems
# Author:      Edison Ying
# Created:     3-Apr-2023
# Updated:     11-Apr-2023
# -----------------------------------------------------------------------------

"""
The scenario that we have is that you are a cashier,
and we are designing a system to tell the cashier the
least amount of coins needed for a customer's change.
We also want to tell the cashier which coins and
how much of those coins will be given back to the customer.
There will be an assumption that there is an
infinite number of each type of coin available to the cashier.
"""

coins = [25, 5, 10] # The type of coins available
combs = []


def comb(V):
    """
    Recursive function that gets all combinations of change

    Note that this is not the most efficient method and it is just a method
    to easily demonstrate recursion. We create a tree by repeating the function
    to see if we have the correct amount of change.

    Parameters
    -----------
    V : int, float
        the value that should be made using the available coins

    Returns
    --------
    str, list
        'IMPOSSIBLE' if the value is unattainable
        list of the combination if value is obtainable
    """
    # Base case
    if V[-1] == 0:
        combs.append(V)
        return V

    result = [1 for i in range(99999)]

    # Try every coin that has smaller value than V
    for coin in coins:
        if coin > V[-1]:
            continue
        new = list(V)
        new.append(V[-1] - coin)
        print(new)
        recur = comb(new)
        if recur == "IMPOSSIBLE":
            continue
        # Check if this is the lowest result
        if len(recur) < len(result):
             result = new
    if len(result) == 99999:
        return "IMPOSSIBLE"
    else:
        return result


value = [float(input("Please enter a value you want: "))]

comb(value)
print(combs)

# Find the best combination of change
if combs == []:
    # Impossible Case
    print("There is no way to get " + str(value) + " with the coins available")
else:
    # Find the least coins required
    smallest = 9999999
    for combination in combs:
        if len(combination) < smallest:
            smallest = len(combination)
            result = combination

    # Finds the number of each coin in the best case
    give = {}
    for i in range(len(result)):
        if i == len(result) - 1:
            break
        dif = round(result[i] - result[i+1], 2)
        if dif in give:
            give[dif] += 1
        else:
            give[dif] = 1
    print(give)
