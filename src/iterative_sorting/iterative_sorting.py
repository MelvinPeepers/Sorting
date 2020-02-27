# Algorithm

# Start with current index = 0 - check

# For all indices EXCEPT the last index: - check

# a. Loop through elements on right-hand-side of current index and find the smallest element

# TO-DO: Complete the selection_sort() function below


def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for j in range(cur_index, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j

        # TO-DO: swap b. Swap the element at current index with the smallest element found in above loop
        # had to google show to swap two variables https://www.programiz.com/python-programming/examples/swap-variables
        arr[smallest_index], arr[cur_index] = arr[cur_index], arr[smallest_index]

    return arr


# TO-DO:  implement the Bubble Sort function below

def swap(arr, index_1, index_2):
    temp = arr[index_1]
    arr[index_1] = arr[index_2]
    arr[index_2] = temp


def bubble_sort(arr):
    # for each pair(elem1, elem2):
    for i in arr:
        # loop that iterates up until the last element of the list
        for index in range(len(arr) - 1):
            #     if elem1 > elem2:
            if arr[index] > arr[index + 1]:
                #         swap(elem1, elem2)
                swap(arr, index, index + 1)

    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):

    return arr
