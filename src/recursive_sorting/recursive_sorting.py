"""
Recursive sorting module
"""


def merge(arr_a, arr_b):
    """
    Merge Sort helper function
    """
    merged_arr = []

    while len(arr_a) > 0 and len(arr_b) > 0:
        if arr_a[0] > arr_b[0]:
            merged_arr.append(arr_b[0])
            arr_b.pop(0)
        else:
            merged_arr.append(arr_a[0])
            arr_a.pop(0)

    while len(arr_a) > 0:
        merged_arr.append(arr_a[0])
        arr_a.pop(0)

    while len(arr_b) > 0:
        merged_arr.append(arr_b[0])
        arr_b.pop(0)
    # TO-DO

    return merged_arr


# print(merge([2, 3, 6], [1, 2]))
# TO-DO: implement the Merge Sort function below USING RECURSION


def merge_sort(arr):
    """
    Merge sort implementation
    """

    if len(arr) <= 1:
        return arr

    half = len(arr)//2

    # Python slice api is bae
    split_a = arr[half:]
    split_b = arr[:half]

    # Recursively split
    split_a = merge_sort(split_a)
    split_b = merge_sort(split_b)

    return merge(split_a, split_b)


# print(merge_sort([8, 9, 1, 4, 12, 6, 133]))
# STRETCH: implement an in-place merge sort algorithm


# def merge_in_place(arr, start, mid, end):
    # """
    # In-Place Merge sort with O(1) space complexity
    # """
    # TO-DO


# def merge_sort_in_place(arr, l, r):
    # TO-DO

    # STRETCH: implement the Timsort function below
    # hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt

    # def timsort(arr):

    #     return arr
