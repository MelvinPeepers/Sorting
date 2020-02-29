# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge(arrA, arrB):
    # create new array of size [len(arrA) + len(arrB)] for merged elements not implementing in place
    elements = len(arrA) + len(arrB)
    # create a new array to hold elements
    merged_arr = [0] * elements
    # TO-DO
    # for all elements:
    # if ALL ELEMENTS IN arrA HAVE BEEN MERGED, put next element in arrB into merged array
    # elif ALL ELEMENTS in arrB have been merged, put next element in arrA into merged array
    # elif next ELEMENT IN arrA SMALLER, add to merged array
    # else next element in arrB smaller, add to merged array

    # return merged array
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # TO-DO
    # if the length of the array is greater then 1
    if len(arr) > 1:
        # we need to "divide" it some more  left hand side of the array, right hand side of the array call the merge sort function
        left = merge_sort(arr[0: len(arr) / 2])
        right = merge_sort(arr[len(arr) / 2:])
        # "conquer" We need to merge the pieces back together (above merge())
        arr = merge(left, right)

    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr
