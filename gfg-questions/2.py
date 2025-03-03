"""Given an array arr[] containing only non-negative integers, your task is to find a continuous subarray (a contiguous sequence of elements) whose sum equals a specified value target. You need to return the 1-based indices of the leftmost and rightmost elements of this subarray. You need to find the first subarray whose sum is equal to the target.

Note: If no such array is possible then, return [-1].
Input: arr[] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], target = 15
Output: [1, 5]
Explanation: The sum of elements from 1st to 5th position is 15.

    """
    
    
def find_subarray(arr, target):
    left, curr_sum = 0, 0  # Initialize left pointer and current sum

    for right in range(len(arr)):  # Expand right pointer
            curr_sum += arr[right]
    
            # Shrink window if sum exceeds target
            while curr_sum > target and left <= right:
                curr_sum -= arr[left]
                left += 1
    
            # Check if the current sum matches the target
            if curr_sum == target:
                return [left + 1, right + 1]  # Convert to 1-based index
    
    return [-1]

# Example usage
# arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# target = 15
arr = [12,18,5,11,30,5]
target = 69
print(find_subarray(arr, target))  # Output: [1, 5]
