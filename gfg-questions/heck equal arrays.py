"""Given two arrays a[] and b[] of equal size, the task is to find whether the elements in the arrays are equal.

    Two arrays are said to be equal if both contain the same set of elements, arrangements (or permutations) of elements may be different though.

Note: If there are repetitions, then counts of repeated elements must also be the same for two arrays to be equal.

Examples:

Input: a[] = [1, 2, 5, 4, 0], b[] = [2, 4, 5, 0, 1]
Output: true
Explanation: Both the array can be rearranged to [0,1,2,4,5]

Input: a[] = [1, 2, 5], b[] = [2, 4, 15]
Output: false
Explanation: a[] and b[] have only one common value."""

def are_arrays_equal(a, b):
    if len(a) != len(b):
        return False  # Arrays must be of the same size

    # Create frequency dictionaries manually
    freq_a = {}
    freq_b = {}

    for num in a:
        freq_a[num] = freq_a.get(num, 0) + 1

    for num in b:
        freq_b[num] = freq_b.get(num, 0) + 1

    return freq_a == freq_b  # Compare both frequency dictionaries

# Test cases
print(are_arrays_equal([1, 2, 5, 4, 0], [2, 4, 5, 0, 1]))  # Output: True
print(are_arrays_equal([1, 2, 5], [2, 4, 15]))            # Output: False
print(are_arrays_equal([1, 2, 2, 3], [3, 2, 1, 2]))       # Output: True
print(are_arrays_equal([1, 2, 2, 3], [3, 2, 1, 1]))       # Output: False
