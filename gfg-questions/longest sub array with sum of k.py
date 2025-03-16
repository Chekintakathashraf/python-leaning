"""Given an array arr[] containing integers and an integer k, your task is to find the length of the longest subarray where the sum of its elements is equal to the given value k. If there is no subarray with sum equal to k, return 0.

Examples:

Input: arr[] = [10, 5, 2, 7, 1, -10], k = 15
Output: 6
Explanation: Subarrays with sum = 15 are [5, 2, 7, 1], [10, 5] and [10, 5, 2, 7, 1, -10]. The length of the longest subarray with a sum of 15 is 6.

Input: arr[] = [-5, 8, -14, 2, 4, 12], k = -5
Output: 5
Explanation: Only subarray with sum = -5 is [-5, 8, -14, 2, 4] of length 5.

Input: arr[] = [10, -10, 20, 30], k = 5
Output: 0
Explanation: No subarray with sum = 5 is present in arr[]."""

def longest_subarray_with_sum_k(arr, k):
    sum_map = {}  # Stores prefix_sum:index
    prefix_sum = 0
    max_length = 0

    for i, num in enumerate(arr):
        prefix_sum += num  # Update cumulative sum

        if prefix_sum == k:  
            max_length = i + 1  # If sum from start to i == k

        if (prefix_sum - k) in sum_map:
            max_length = max(max_length, i - sum_map[prefix_sum - k])

        if prefix_sum not in sum_map:  
            sum_map[prefix_sum] = i  # Store first occurrence of prefix_sum

    return max_length

# Test Cases
print(longest_subarray_with_sum_k([10, 5, 2, 7, 1, -10], 15))  # Output: 6
print(longest_subarray_with_sum_k([-5, 8, -14, 2, 4, 12], -5))  # Output: 5
print(longest_subarray_with_sum_k([10, -10, 20, 30], 5))  # Output: 0
