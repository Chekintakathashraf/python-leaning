"""Given an array arr[] denoting heights of N towers and a positive integer K.

For each tower, you must perform exactly one of the following operations exactly once.

    Increase the height of the tower by K
    Decrease the height of the tower by K

Find out the minimum possible difference between the height of the shortest and tallest towers after you have modified each tower.

You can find a slight modification of the problem here.
Note: It is compulsory to increase or decrease the height by K for each tower. After the operation, the resultant array should not contain any negative integers.

Examples :

Input: k = 2, arr[] = {1, 5, 8, 10}
Output: 5
Explanation: The array can be modified as {1+k, 5-k, 8-k, 10-k} = {3, 3, 6, 8}.The difference between the largest and the smallest is 8-3 = 5.

Input: k = 3, arr[] = {3, 9, 12, 16, 20}
Output: 11
Explanation: The array can be modified as {3+k, 9+k, 12-k, 16-k, 20-k} -> {6, 12, 9, 13, 17}.The difference between the largest and the smallest is 17-6 = 11. 
"""


def min_height_difference(arr, k):
    n = len(arr)
    if n == 1:
        return 0  # Only one tower, no height difference

    arr.sort()  # Step 1: Sort the array

    # Initial difference (before modifying heights)
    min_diff = arr[-1] - arr[0]

    # Set smallest and largest heights
    smallest = arr[0] + k
    largest = arr[-1] - k

    if smallest > largest:  
        smallest, largest = largest, smallest

    # Traverse the sorted array
    for i in range(1, n):
        min_height = min(smallest, arr[i] - k)
        max_height = max(largest, arr[i - 1] + k)

        if min_height < 0:
            continue  # Ignore negative heights

        min_diff = min(min_diff, max_height - min_height)

    return min_diff

# Test Cases
print(min_height_difference([1, 5, 8, 10], 2))  # Output: 5
print(min_height_difference([3, 9, 12, 16, 20], 3))  # Output: 11
