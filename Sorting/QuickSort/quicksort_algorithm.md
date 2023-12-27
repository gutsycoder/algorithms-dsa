# Quick Sort Algorithm using Recursion

`QuickSort` is a `Divide and Conquer algorithm`. It picks an element as a pivot and partitions the given array around the pivot. There are many different versions of quickSort that pick the pivot in different ways. 

*Always pick the first element as a pivot.
*Always pick the last element as a pivot.
*Pick a random element as a pivot.
*Pick the median as the pivot.

`Note: Here we have implemented quick sort by picking the first element as the pivot`.

# Explanation of the Quick Sort algorithm

# 1. Choose a Pivot:
   - The `quickSort` function selects the first element (`arr[low]`) as the pivot.

# 2. Partition:
   - The `pivotGetsSorted` function performs the partitioning:
     - It creates two pointers, `first` (starting at index `low + 1`) and `last` (starting at the end of the array, `high`).
     - It iterates through the array using a `while` loop:
       - It moves `first` forward until it finds an element greater than the pivot.
       - It moves `last` backward until it finds an element less than or equal to the pivot.
       - If `first` is still less than or equal to `last`, it swaps `arr[first]` and `arr[last]`.
     - It swaps the pivot (`arr[low]`) with `arr[last]` to place the pivot in its correct position.
     - It returns the final position of the pivot (`last`).

# 3. Recursive Calls:
   - The `quickSort` function recursively calls itself on the left subarray (`arr[low : partition_index - 1]`) and the right subarray (`arr[partition_index + 1 : high]`).

# 4. Repetition:
   - The recursive calls continue until all subarrays are sorted, resulting in the entire array being sorted.

**Example:**

- Assuming `arr = [8, 5, 2, 9, 5, 6, 3]`:
   - The initial `pivot` is `8`.
   - After partitioning, `arr` becomes `[5, 2, 5, 6, 3, 8, 9]`.
   - Recursive calls sort the left and right subarrays.
   - The final sorted array is `[2, 3, 5, 5, 6, 8, 9]`.