def linear_search(array, desired):
    """
    Linear search algorithm to find an element in an array

    Parameters
    -----------
    array : list
        the list used in the search
    desired : str
        the item to be found in the list

    Returns
    --------
    int : the index of the item, -1 if it is not found

    """
    for i in range(len(array)):
        if array[i].name == desired:
            return i
    return -1


def binary_search(array, x):
    low = 0
    high = len(array) - 1
    mid = 0

    while low <= high:

        mid = (high + low) // 2

        # If x is greater, ignore left half
        if array[mid].population < x:
            low = mid + 1

        # If x is smaller, ignore right half
        elif array[mid].population > x:
            high = mid - 1

        # means x is present at mid
        else:
            return mid

    # If we reach here, then the element was not present
    return -1