"""
Iterative sorting algorithms
"""


def selection_sort(arr):
    """
    Selection sort implementation
    """
    for i in range(0, len(arr) - 1):
        smallest_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]
    return arr


def bubble_sort(arr):
    """
    Bubble sort implementation
    """
    for i in range(0, len(arr)):
        for j in range(i+1, len(arr)):
            if arr[j] < arr[i]:
                arr[j], arr[i] = arr[i], arr[j]

    return arr


# STRETCH: implement the Count Sort function below


def count_sort(arr, maximum=-1):
    """
    Count sort implementation - Stretch
    """

    return arr
