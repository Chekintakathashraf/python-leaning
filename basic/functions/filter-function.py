# Example 1: Filter even numbers from a list
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Output: [2, 4, 6]

# Example 2: Filter odd numbers from a list
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
print(odd_numbers)  # Output: [1, 3, 5]

# Example 3: Filter positive numbers from a list
numbers = [-1, 2, -3, 4, -5, 6]
positive_numbers = list(filter(lambda x: x > 0, numbers))
print(positive_numbers)  # Output: [2, 4, 6]

# Example 4: Filter negative numbers from a list
negative_numbers = list(filter(lambda x: x < 0, numbers))
print(negative_numbers)  # Output: [-1, -3, -5]

# Example 5: Filter strings with length greater than 3
strings = ["apple", "bat", "cat", "dog", "elephant"]
long_strings = list(filter(lambda x: len(x) > 3, strings))
print(long_strings)  # Output: ['apple', 'elephant']

# Example 6: Filter strings that start with 'a'
a_strings = list(filter(lambda x: x.startswith('a'), strings))
print(a_strings)  # Output: ['apple']

# Example 7: Filter strings that end with 't'
t_strings = list(filter(lambda x: x.endswith('t'), strings))
print(t_strings)  # Output: ['bat', 'cat', 'elephant']

# Example 8: Filter prime numbers from a list
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10]
prime_numbers = list(filter(is_prime, numbers))
print(prime_numbers)  # Output: [2, 3, 5, 7]

# Example 9: Filter palindromes from a list of strings
strings = ["madam", "racecar", "hello", "world", "level"]
palindromes = list(filter(lambda x: x == x[::-1], strings))
print(palindromes)  # Output: ['madam', 'racecar', 'level']

# Example 10: Filter numbers greater than a given value
numbers = [1, 2, 3, 4, 5, 6]
greater_than_3 = list(filter(lambda x: x > 3, numbers))
print(greater_than_3)  # Output: [4, 5, 6]

# Example 11: Filter numbers less than a given value
less_than_4 = list(filter(lambda x: x < 4, numbers))
print(less_than_4)  # Output: [1, 2, 3]

# Example 12: Filter non-empty strings
strings = ["apple", "", "banana", "", "cherry"]
non_empty_strings = list(filter(lambda x: x != "", strings))
print(non_empty_strings)  # Output: ['apple', 'banana', 'cherry']

# Example 13: Filter non-zero numbers
numbers = [0, 1, 2, 0, 3, 0, 4]
non_zero_numbers = list(filter(lambda x: x != 0, numbers))
print(non_zero_numbers)  # Output: [1, 2, 3, 4]

# Example 14: Filter numbers that are multiples of 3
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
multiples_of_3 = list(filter(lambda x: x % 3 == 0, numbers))
print(multiples_of_3)  # Output: [3, 6, 9]

# Example 15: Filter numbers that are multiples of 5
multiples_of_5 = list(filter(lambda x: x % 5 == 0, numbers))
print(multiples_of_5)  # Output: [5]

# Example 16: Filter uppercase strings
strings = ["Apple", "banana", "Cherry", "date"]
uppercase_strings = list(filter(lambda x: x[0].isupper(), strings))
print(uppercase_strings)  # Output: ['Apple', 'Cherry']

# Example 17: Filter lowercase strings
lowercase_strings = list(filter(lambda x: x[0].islower(), strings))
print(lowercase_strings)  # Output: ['banana', 'date']

# Example 18: Filter strings containing a specific substring
strings = ["apple", "banana", "cherry", "date"]
contains_an = list(filter(lambda x: 'an' in x, strings))
print(contains_an)  # Output: ['banana']

# Example 19: Filter strings with only alphabetic characters
strings = ["apple", "banana123", "cherry", "date!"]
alphabetic_strings = list(filter(lambda x: x.isalpha(), strings))
print(alphabetic_strings)  # Output: ['apple', 'cherry']

# Example 20: Filter strings with only numeric characters
strings = ["123", "abc", "456", "789xyz"]
numeric_strings = list(filter(lambda x: x.isdigit(), strings))
print(numeric_strings)  # Output: ['123', '456']

# Example 21: Filter strings with only alphanumeric characters
strings = ["apple123", "banana!", "cherry456", "date"]
alphanumeric_strings = list(filter(lambda x: x.isalnum(), strings))
print(alphanumeric_strings)  # Output: ['apple123', 'cherry456', 'date']

# Example 22: Filter strings with only whitespace characters
strings = ["   ", "apple", "\t", "banana", "\n"]
whitespace_strings = list(filter(lambda x: x.isspace(), strings))
print(whitespace_strings)  # Output: ['   ', '\t', '\n']

# Example 23: Filter strings with only uppercase characters
strings = ["APPLE", "banana", "CHERRY", "DATE"]
uppercase_only_strings = list(filter(lambda x: x.isupper(), strings))
print(uppercase_only_strings)  # Output: ['APPLE', 'CHERRY', 'DATE']

# Example 24: Filter strings with only lowercase characters
lowercase_only_strings = list(filter(lambda x: x.islower(), strings))
print(lowercase_only_strings)  # Output: ['banana']

# Example 25: Filter strings with only title case characters
strings = ["Apple", "Banana", "cherry", "Date"]
title_case_strings = list(filter(lambda x: x.istitle(), strings))
print(title_case_strings)  # Output: ['Apple', 'Banana', 'Date']

# Example 26: Filter strings with only printable characters
strings = ["apple", "banana\n", "cherry\t", "date"]
printable_strings = list(filter(lambda x: x.isprintable(), strings))
print(printable_strings)  # Output: ['apple', 'date']

# Example 27: Filter strings with only ASCII characters
strings = ["apple", "banana", "cherry", "date", "élan"]
ascii_strings = list(filter(lambda x: x.isascii(), strings))
print(ascii_strings)  # Output: ['apple', 'banana', 'cherry', 'date']

# Example 28: Filter strings with only decimal characters
strings = ["123", "456.78", "789", "abc"]
decimal_strings = list(filter(lambda x: x.isdecimal(), strings))
print(decimal_strings)  # Output: ['123', '789']

# Example 29: Filter strings with only digit characters
digit_strings = list(filter(lambda x: x.isdigit(), strings))
print(digit_strings)  # Output: ['123', '456', '789']

# Example 30: Filter strings with only numeric characters
numeric_strings = list(filter(lambda x: x.isnumeric(), strings))
print(numeric_strings)  # Output: ['123', '456', '789']