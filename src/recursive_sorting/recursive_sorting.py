# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = []  # a new empty list. add members of left and right to result unit it contains a sorted list with elements of both
    # TO-DO
    while (arrA and arrB):  # create a loop that will continue iterating while both arrA and arrB have elements
        if arrA[0] < arrB[0]:  # check if first element of left is smaller then the first element of right
            elements.append(arrA[0])  # append arrA[0] to our elements list
            arrA.pop(0)  # remove the first element from the left list
        else:
            elements.append(arrB[0])
            arrB.pop(0)
    if arrA:
        elements += arrA  # check if there are any elements still in arrA. If there are, add them to the end of the elements
    if arrB:
        elements += arrB  # check if there are any elements still in arrB. If there are, add them to the end of the elements
        # return merged array
    return elements


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # TO-DO
    # if the length of the array is greater then 1
    if len(arr) > 1:
        # we need to "divide" it some more  left hand side of the array, right hand side of the array call the merge sort function
        left = merge_sort(arr[0: len(arr) // 2])
        right = merge_sort(arr[len(arr) // 2:])
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
