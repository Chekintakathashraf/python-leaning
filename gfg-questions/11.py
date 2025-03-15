"""Given an array arr. Find the majority element in the array. If no majority exists, return -1.

    A majority element in an array is an element that appears strictly more than arr.size()/2 times in the array.

Examples:

Input: arr[] = [3, 1, 3, 3, 2]
Output: 3
Explanation: Since, 3 is present more than n/2 times, so it is the majority element.

Input: arr[] = [7]
Output: 7
Explanation: Since, 7 is single element and present more than n/2 times, so it is the majority element.

Input: arr[] = [2, 13]
Output: -1
Explanation: Since, no element is present more than n/2 times, so there is no majority element.

Expected Time Complexity: O(n)
Expected Auxiliary Space: O(1)"""


def majority_element(arr):
    n = len(arr)
    candidate, count = None, 0

    # First pass: Find the candidate
    for num in arr:
        if count == 0:
            candidate = num
            count = 1
        elif num == candidate:
            count += 1
        else:
            count -= 1

    # Second pass: Verify the candidate
    if arr.count(candidate) > n // 2:
        return candidate
    return -1

# Test Cases
print(majority_element([3, 1, 3, 3, 2]))  # Output: 3
print(majority_element([7]))  # Output: 7
print(majority_element([2, 13]))  # Output: -1


