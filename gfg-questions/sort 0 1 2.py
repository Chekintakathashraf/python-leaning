"""Given an array arr[] containing only 0s, 1s, and 2s. Sort the array in ascending order.

You need to solve this problem without utilizing the built-in sort function.

Examples:

Input: arr[] = [0, 1, 2, 0, 1, 2]
Output: [0, 0, 1, 1, 2, 2]
Explanation: 0s 1s and 2s are segregated into ascending order.

Input: arr[] = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]
Output: [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2]
Explanation: 0s 1s and 2s are segregated into ascending order.

Follow up: Could you come up with a one-pass algorithm using only constant extra space?"""



def sort_colors(arr):
    low, mid, high = 0, 0, len(arr) - 1

    while mid <= high:
        if arr[mid] == 0:  # Move 0s to the left
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:  # Keep 1s in the middle
            mid += 1
        else:  # Move 2s to the right
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1  # Decrement high, but do not increment mid

    return arr

# Test Cases
print(sort_colors([0, 1, 2, 0, 1, 2]))  # Output: [0, 0, 1, 1, 2, 2]
print(sort_colors([0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]))  # Output: [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2]
