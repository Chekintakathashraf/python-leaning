"""
    Given an integer array arr[]. You need to find the maximum sum of a subarray.
    Input: arr[] = [2, 3, -8, 7, -1, 2, 3]
Output: 11
Explanation: The subarray {7, -1, 2, 3} has the largest sum 11.

Input: arr[] = [-2, -4]
Output: -2
Explanation: The subarray {-2} has the largest sum -2.

Input: arr[] = [5, 4, 1, 7, 8]
Output: 25
Explanation: The subarray {5, 4, 1, 7, 8} has the largest sum 25.

Kadane's Algorithm

What is a Maximum Subarray?

A maximum subarray is the contiguous subarray within an array that has the largest sum.
    
    """
    
    
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

"""
Subarray	    Sum
[-2]	        -2
[1]	             1
[1, -3]	        -2
[4]	             4
[4, -1]     	 3
[4, -1, 2]	     5
[4, -1, 2, 1]	 6 ✅ (Maximum Sum)
[-5]	        -5
[4]	             4
    """
    
    
def max_subarray_sum(arr):
    max_sum = 0  # Initialize with smallest possible value
    current_sum = 0
    
    for num in arr:
        current_sum += num
        max_sum = max(max_sum, current_sum)
        
        # Reset if current_sum drops below 0
        if current_sum < 0:
            current_sum = 0  

    return max_sum

# Test cases
print(max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # Output: 6 (subarray [4, -1, 2, 1])
print(max_subarray_sum([1, 2, 3, 4]))  # Output: 10 (subarray [1, 2, 3, 4])
print(max_subarray_sum([-1, -2, -3, -4]))  # Output: -1 (single element [-1])
