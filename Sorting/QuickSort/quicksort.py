# IMPLEMENTATION OF QUICK SORT ALGORITHM RECURSIVELY
# SOURCE: https://www.geeksforgeeks.org/implement-quicksort-with-first-element-as-pivot/


import random
arr = random.sample(range(-20, 20), 10)  # Generate test cases (integers only)

def quickSort(arr, low, high):
    if low < high:
        partition_index = pivotGetsSorted(arr, low, high)
        quickSort(arr, low, partition_index - 1)
        quickSort(arr, partition_index + 1, high)

def pivotGetsSorted(arr, low, high):
    pivot = arr[low]
    first = low + 1
    last = high

    while first <= last:
        while first <= last and arr[first] <= pivot:
            first += 1
        while first <= last and arr[last] > pivot:
            last -= 1
        if first <= last:
            arr[first], arr[last] = arr[last], arr[first]

    arr[low], arr[last] = arr[last], arr[low]
    return last

quickSort(arr, 0, len(arr) - 1) 

# if arr == sorted(arr): #verify the test case pass or not
#     print(True)
# else:
#     print(False)

print(arr)