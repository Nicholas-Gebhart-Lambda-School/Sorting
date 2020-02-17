"""
Recursive sorting module
"""


def merge(arrA, arrB):
    """
    Merge Sort helper function
    """
    merged_arr = []

    while len(arrA) > 0 and len(arrB) > 0:
        if arrA[0] > arrB[0]:
            merged_arr.append(arrB[0])
            arrB.pop(0)
        merged_arr.append(arrA[0])
        arrA.pop(0)

    while len(arrA) > 0:
        merged_arr.append(arrA[0])
        arrA.pop(0)

    while len(arrB) > 0:
        merged_arr.append(arrB[0])
        arrB.pop(0)
    # TO-DO

    return merged_arr


# print(merge([2, 3, 6], [1, 2]))
# TO-DO: implement the Merge Sort function below USING RECURSION


def merge_sort(arr):
    """
    Merge sort implementation
    """
    # TO-DO
    base = len(arr)

    # Once our arrays have been reduced to
    # A single element
    if base == 1:
        return arr

    half = base//2

    # Python slice api is bae
    split_a = arr[half:]
    split_b = arr[:half]

    # Recursively split
    split_a = merge_sort(split_a)
    split_b = merge_sort(split_b)

    return merge(split_a, split_b)


print(merge_sort([8, 9, 1, 4, 12, 6, 133]))
# STRETCH: implement an in-place merge sort algorithm


def merge_in_place(arr, start, mid, end):
    """
    In-Place Merge sort with O(1) space complexity
    """
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr
