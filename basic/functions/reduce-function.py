from functools import reduce
import math

# Example 1: Sum of a list of numbers
numbers = [1, 2, 3, 4, 5]
result = reduce(lambda x, y: x + y, numbers)
print(result)  # Output: 15

# Example 2: Product of a list of numbers
result = reduce(lambda x, y: x * y, numbers)
print(result)  # Output: 120

# Example 3: Maximum of a list of numbers
result = reduce(lambda x, y: x if x > y else y, numbers)
print(result)  # Output: 5

# Example 4: Minimum of a list of numbers
result = reduce(lambda x, y: x if x < y else y, numbers)
print(result)  # Output: 1

# Example 5: Concatenate a list of strings
strings = ["Hello", " ", "World", "!"]
result = reduce(lambda x, y: x + y, strings)
print(result)  # Output: "Hello World!"

# Example 6: Flatten a list of lists
lists = [[1, 2], [3, 4], [5, 6]]
result = reduce(lambda x, y: x + y, lists)
print(result)  # Output: [1, 2, 3, 4, 5, 6]

# Example 7: Find the longest string in a list
strings = ["short", "longer", "longest"]
result = reduce(lambda x, y: x if len(x) > len(y) else y, strings)
print(result)  # Output: "longest"

# Example 8: Find the shortest string in a list
result = reduce(lambda x, y: x if len(x) < len(y) else y, strings)
print(result)  # Output: "short"

# Example 9: Calculate the sum of squares of a list of numbers
result = reduce(lambda x, y: x + y**2, numbers, 0)
print(result)  # Output: 55

# Example 10: Calculate the factorial of a number
n = 5
result = reduce(lambda x, y: x * y, range(1, n + 1))
print(result)  # Output: 120

# Example 11: Calculate the greatest common divisor (GCD) of a list of numbers
numbers = [48, 64, 16]
result = reduce(math.gcd, numbers)
print(result)  # Output: 16

# Example 12: Calculate the least common multiple (LCM) of a list of numbers
def lcm(x, y):
    return x * y // math.gcd(x, y)
numbers = [4, 6, 8]
result = reduce(lcm, numbers)
print(result)  # Output: 24

# Example 13: Find the longest word in a sentence
sentence = "The quick brown fox jumps over the lazy dog"
words = sentence.split()
result = reduce(lambda x, y: x if len(x) > len(y) else y, words)
print(result)  # Output: "jumps"

# Example 14: Find the shortest word in a sentence
result = reduce(lambda x, y: x if len(x) < len(y) else y, words)
print(result)  # Output: "The"

# Example 15: Calculate the sum of digits of a number
number = 12345
digits = [int(digit) for digit in str(number)]
result = reduce(lambda x, y: x + y, digits)
print(result)  # Output: 15

# Example 16: Calculate the product of digits of a number
result = reduce(lambda x, y: x * y, digits)
print(result)  # Output: 120

# Example 17: Calculate the sum of even numbers in a list
result = reduce(lambda x, y: x + y if y % 2 == 0 else x, numbers, 0)
print(result)  # Output: 12

# Example 18: Calculate the product of odd numbers in a list
result = reduce(lambda x, y: x * y if y % 2 != 0 else x, numbers, 1)
print(result)  # Output: 15

# Example 19: Calculate the sum of squares of even numbers in a list
result = reduce(lambda x, y: x + y**2 if y % 2 == 0 else x, numbers, 0)
print(result)  # Output: 56

# Example 20: Calculate the product of squares of odd numbers in a list
result = reduce(lambda x, y: x * y**2 if y % 2 != 0 else x, numbers, 1)
print(result)  # Output: 225

# Example 21: Calculate the sum of cubes of a list of numbers
result = reduce(lambda x, y: x + y**3, numbers, 0)
print(result)  # Output: 225

# Example 22: Calculate the product of cubes of a list of numbers
result = reduce(lambda x, y: x * y**3, numbers, 1)
print(result)  # Output: 1728000

# Example 23: Calculate the sum of reciprocals of a list of numbers
result = reduce(lambda x, y: x + 1/y, numbers, 0)
print(result)  # Output: 2.283333333333333

# Example 24: Calculate the product of reciprocals of a list of numbers
result = reduce(lambda x, y: x * 1/y, numbers, 1)
print(result)  # Output: 0.008333333333333333

# Example 25: Calculate the sum of factorials of a list of numbers
result = reduce(lambda x, y: x + math.factorial(y), numbers, 0)
print(result)  # Output: 153

# Example 26: Calculate the product of factorials of a list of numbers
result = reduce(lambda x, y: x * math.factorial(y), numbers, 1)
print(result)  # Output: 34560

# Example 27: Calculate the sum of the lengths of strings in a list
strings = ["apple", "banana", "cherry"]
result = reduce(lambda x, y: x + len(y), strings, 0)
print(result)  # Output: 16

# Example 28: Calculate the product of the lengths of strings in a list
result = reduce(lambda x, y: x * len(y), strings, 1)
print(result)  # Output: 30

# Example 29: Calculate the sum of ASCII values of characters in a string
string = "abc"
result = reduce(lambda x, y: x + ord(y), string, 0)
print(result)  # Output: 294

# Example 30: Calculate the product of ASCII values of characters in a string
result = reduce(lambda x, y: x * ord(y), string, 1)
print(result)  # Output: 941094

# Example 31: Calculate the sum of the squares of the lengths of strings in a list
result = reduce(lambda x, y: x + len(y)**2, strings, 0)
print(result)  # Output: 86

# Example 32: Calculate the product of the squares of the lengths of strings in a list
result = reduce(lambda x, y: x * len(y)**2, strings, 1)
print(result)  # Output: 900

# Example 33: Calculate the sum of the cubes of the lengths of strings in a list
result = reduce(lambda x, y: x + len(y)**3, strings, 0)
print(result)  # Output: 432

# Example 34: Calculate the product of the cubes of the lengths of strings in a list
result = reduce(lambda x, y: x * len(y)**3, strings, 1)
print(result)  # Output: 27000

# Example 35: Calculate the sum of the reciprocals of the lengths of strings in a list
result = reduce(lambda x, y: x + 1/len(y), strings, 0)
print(result)  # Output: 0.7833333333333333

# Example 36: Calculate the product of the reciprocals of the lengths of strings in a list
result = reduce(lambda x, y: x * 1/len(y), strings, 1)
print(result)  # Output: 0.005555555555555556