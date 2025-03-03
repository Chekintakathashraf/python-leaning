"""You are given a number n. You need to generate and print a pattern based on the given value of n.

    For each row, starting from the first, print numbers in descending order from n down to 1.
    Each number in a row is repeated as many times as the current row index (starting from n).
    Instead of printing each row on a new line, separate rows with -1.
    Instead of a newline at the end of each row, print -1 to indicate row separation. After printing the entire pattern, end the output with -1. Input: 3
Output: [3, 3, 3, 2, 2, 2, 1, 1, 1, -1, 3, 3, 2, 2, 1, 1, -1, 3, 2, 1, -1] Constraints:
1 <= n <= 40"""

def generate_pattern(n):
    result = []
    for i in range(n, 0, -1):
        for j in range(n, 0, -1):
            result.extend([j] * i)
        result.append(-1)
    return result

# Example usage
n = int(input("Enter n: "))  # Input value for n
print(generate_pattern(n))
