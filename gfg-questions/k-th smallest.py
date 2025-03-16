"""Given an array arr[] and an integer k where k is smaller than the size of the array, the task is to find the kth smallest element in the given array.

Follow up: Don't solve it using the inbuilt sort function.

Examples :

Input: arr[] = [7, 10, 4, 3, 20, 15], k = 3
Output:  7
Explanation: 3rd smallest element in the given array is 7.

Input: arr[] = [2, 3, 1, 20, 15], k = 4 
Output: 15
Explanation: 4th smallest element in the given array is 15.

Expected Time Complexity: O(n+(max_element) )
Expected Auxiliary Space: O(max_element)"""


def kth_smallest(arr, k):
    left, right = 0, len(arr) - 1

    while left <= right:
        pivot = arr[right]  # Choose the last element as pivot
        i = left  # Pointer for placing smaller elements

        for j in range(left, right):  # Partition step
            if arr[j] <= pivot:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1

        arr[i], arr[right] = arr[right], arr[i]  # Place pivot at correct position

        if i == k - 1:  # If pivot is kth smallest
            return arr[i]
        elif i > k - 1:  # Search in left part
            right = i - 1
        else:  # Search in right part
            left = i + 1

    return -1  # Should not reach here if k is valid

# Test Cases
print(kth_smallest([7, 10, 4, 3, 20, 15], 3))  # Output: 7
print(kth_smallest([2, 3, 1, 20, 15], 4))  # Output: 15
