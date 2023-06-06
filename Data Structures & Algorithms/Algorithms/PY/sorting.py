def insertionSort(array):
    """
    Sorts an array in ascending order

    Parameters:
        array (array) the array to sort

    Returns:
        (array): the sorted array
    """

    length = len(array)
    for i in range(1, length):
        # print(i)
        # use the current array item as a key to compare
        key = array[i].get_population()
        original = array[i]
        # print(key)

        # set index to start comparison with
        j = i - 1
        pop = array[j].get_population()
        # find a spot in the left sublist for the key to go
        while j >= 0 and pop > key:
            # array[j + 1] = array[j]
            j = j - 1
            pop = array[j].get_population()

        if j != i:
            array.pop(i)
            array.insert(j+1, original)
        # set the key in the right spot
        # array[j + 1] = original
    return array


def test(array):
    """
    Sorts an array in ascending order

    Parameters:
        array (array) the array to sort

    Returns:
        (array): the sorted array
    """

    length = len(array)
    for i in range(1, length):
        # use the current array item as a key to compare
        key = array[i]

        # set index to start comparison with
        j = i - 1
        # find a spot in the left sublist for the key to go
        while j >= 0 and array[j] > key:
            # array[j + 1] = array[j]
            j = j - 1

        if j != i-1:
            array.pop(i)
            array.insert(j+1, key)
        # set the key in the right spot
        # array[j + 1] = key
    return array