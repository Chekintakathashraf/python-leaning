"""Given a sorted array arr[] of distinct integers. Sort the array into a wave-like array(In Place). In other words, arrange the elements into a sequence such that arr[1] >= arr[2] <= arr[3] >= arr[4] <= arr[5].....
If there are multiple solutions, find the lexicographically smallest one.

Note: The given array is sorted in ascending order, and you don't need to return anything to change the original array.

Examples:

Input: arr[] = [1, 2, 3, 4, 5]
Output: [2, 1, 4, 3, 5]
Explanation: Array elements after sorting it in the waveform are 2, 1, 4, 3, 5.

Input: arr[] = [2, 4, 7, 8, 9, 10]
Output: [4, 2, 8, 7, 10, 9]
Explanation: Array elements after sorting it in the waveform are 4, 2, 8, 7, 10, 9.

Input: arr[] = [1]
Output: [1] """


def convertToWave(arr):
    n = len(arr)
    for i in range(1, n, 2):
        arr[i], arr[i-1] = arr[i-1], arr[i]

# Example Usage:
arr1 = [1, 2, 3, 4, 5]
convertToWave(arr1)
print(arr1)  # Output: [2, 1, 4, 3, 5]

arr2 = [2, 4, 7, 8, 9, 10]
convertToWave(arr2)
print(arr2)  # Output: [4, 2, 8, 7, 10, 9]

arr3 = [1]
convertToWave(arr3)
print(arr3)  # Output: [1]
