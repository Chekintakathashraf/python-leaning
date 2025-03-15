"""You are given an array arr[] of non-negative numbers. Each number tells you the maximum number of steps you can jump forward from that position.

For example:

    If arr[i] = 3, you can jump to index i + 1, i + 2, or i + 3 from position i.
    If arr[i] = 0, you cannot jump forward from that position.

Your task is to find the minimum number of jumps needed to move from the first position in the array to the last position.

Note:  Return -1 if you can't reach the end of the array.

Input: arr[] = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
Output: 3 
Explanation: First jump from 1st element to 2nd element with value 3. From here we jump to 5th element with value 9, and from here we will jump to the last. 

Input: arr = [1, 4, 3, 2, 6, 7]
Output: 2 
Explanation: First we jump from the 1st to 2nd element and then jump to the last element.

Input: arr = [0, 10, 20]
Output: -1
Explanation: We cannot go anywhere from the 1st element.



    """
    
def min_jumps(arr):
    n = len(arr)
    if n <= 1:
        return 0  # Already at the last index
    if arr[0] == 0:
        return -1  # Cannot move forward
    
    jumps = 0
    current_end = 0
    farthest = 0
    
    for i in range(n - 1):  # We don't need to check the last index
        farthest = max(farthest, i + arr[i])
        
        if i == current_end:  # Need to take a jump
            jumps += 1
            current_end = farthest
            
            if current_end >= n - 1:  # Reached or exceeded the last index
                return jumps
    
    return -1  # If we never reach the last index

# Test Cases
print(min_jumps([1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]))  # Output: 3
print(min_jumps([1, 4, 3, 2, 6, 7]))  # Output: 2
print(min_jumps([0, 10, 20]))  # Output: -1

    
    
    
    
    
    