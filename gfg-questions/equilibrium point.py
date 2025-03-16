"""Given an array of integers arr[], the task is to find the first equilibrium point in the array.

The equilibrium point in an array is an index (0-based indexing) such that the sum of all elements before that index is the same as the sum of elements after it. Return -1 if no such point exists. 

Examples:

Input: arr[] = [1, 2, 0, 3]
Output: 2 
Explanation: The sum of left of index 2 is 1 + 2 = 3 and sum on right of index 2 is 3.

Input: arr[] = [1, 1, 1, 1]
Output: -1
Explanation: There is no equilibrium index in the array.

Input: arr[] = [-7, 1, 5, 2, -4, 3, 0]
Output: 3
Explanation: The sum of left of index 3 is -7 + 1 + 5 = -1 and sum on right of index 3 is -4 + 3 + 0 = -1."""

def find_equilibrium_index(arr):
    total_sum = sum(arr)  # Step 1: Compute total sum
    left_sum = 0          # Initialize left sum

    for i in range(len(arr)):
        if left_sum == total_sum - left_sum - arr[i]:  # Check equilibrium condition
            return i
        left_sum += arr[i]  # Update left sum

    return -1  # No equilibrium index found

# Test Cases
print(find_equilibrium_index([1, 2, 0, 3]))  # Output: 2
print(find_equilibrium_index([1, 1, 1, 1]))  # Output: -1
print(find_equilibrium_index([-7, 1, 5, 2, -4, 3, 0]))  # Output: 3
