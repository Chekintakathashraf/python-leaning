"""You are given an array arr of size n - 1 that contains distinct integers in the range from 1 to n (inclusive). This array represents a permutation of the integers from 1 to n with one element missing. Your task is to identify and return the missing element.

Input: arr[] = [1, 2, 3, 5]
Output: 4
Explanation: All the numbers from 1 to 5 are present except 4.

Input: arr[] = [8, 2, 4, 5, 3, 7, 1]
Output: 6
Explanation: All the numbers from 1 to 8 are present except 6.

Input: arr[] = [1]
Output: 2
Explanation: Only 1 is present so the missing element is 2.

Constraints:
1 ≤ arr.size() ≤ 106
1 ≤ arr[i] ≤ arr.size() + 1"""



def missingnumber(arr):
    n = len(arr) + 1
    total = n * (n + 1) // 2
    return total - sum(arr)
#or

# def missingnumber(arr):
#     total_of_arr = sum(arr)
#     total_wanted = sum(range(1,len(arr)+2))
    
#     result = total_wanted - total_of_arr
    
#     return result

""" 1 st method is good since 


    Time Complexity
        Using sum(range(1, n + 1)) is O(n) because it generates and sums the entire range.
        Using n * (n + 1) // 2 is O(1) because it's a simple mathematical formula.
        Best Choice: O(1) approach is better for large values of n (up to 10^6).

    Space Complexity
        Both approaches use O(1) space, so there's no difference.

    Efficiency for Large Inputs
        The formula version is significantly faster and doesn't need to create a list, making it better for performance."""


# arr = [8, 2, 4, 5, 3, 7, 1]
arr = [1, 2, 3, 5]
print(missingnumber(arr))  


