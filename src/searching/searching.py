
"""
Searching module
"""

# STRETCH: implement Linear Search


def linear_search(arr, target):
    """
    Linear Search implementation
    """
    for i in range(0, len(arr)):
        if arr[i] == target:
            return i

    # TO-DO: add missing code

    return -1   # not found


# STRETCH: write an iterative implementation of Binary Search


def binary_search(arr, target):
    """
    Binary Search implementation
    """

    if len(arr) == 0:
        return -1  # array empty

    low = 0
    high = len(arr)-1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    # TO-DO: add missing code

    return -1  # not found


# STRETCH: write a recursive implementation of Binary Search


def binary_search_recursive(arr, target, low, high):
    """
    Recursive Binary Search

    If high is >= low is our base case to break out of the loop

    If our target matches arr[mid] return mid, huzzah!

    If our target value is less than arr[mid], our target element
    cannot exist in the high part of the array, so search backwards
    from the middle element

    Otherwise, search forwards from the middle towards the high index
    until we've either exhausted the array or found a matching mid
    """

    if len(arr) == 0:
        return -1  # array empty

    if high >= low:
        mid = low + (high - low) // 2

        if arr[mid] == target:
            return mid

        if arr[mid] > target:
            return binary_search_recursive(arr, target, low, mid - 1)
        return binary_search_recursive(arr, target, mid + 1, high)
    return -1


# arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# length = len(arr)-1

# print(binary_search_recursive(arr, 8, 0, length))

