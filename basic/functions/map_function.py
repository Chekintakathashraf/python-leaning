# Example 1: Square of numbers
def square(x):
    return x * x

numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(square, numbers))
print(squared_numbers)

# Example 2: Convert to uppercase
def to_uppercase(s):
    return s.upper()

strings = ['hello', 'world']
uppercase_strings = list(map(to_uppercase, strings))
print(uppercase_strings)

# Example 3: Add two lists
def add(x, y):
    return x + y

list1 = [1, 2, 3]
list2 = [4, 5, 6]
added_lists = list(map(add, list1, list2))
print(added_lists)

# Example 4: Convert to string
def to_string(x):
    return str(x)

numbers = [1, 2, 3, 4, 5]
string_numbers = list(map(to_string, numbers))
print(string_numbers)

# Example 5: Length of strings
def length(s):
    return len(s)

strings = ['apple', 'banana', 'cherry']
lengths = list(map(length, strings))
print(lengths)

# Example 6: Multiply by 10
def multiply_by_10(x):
    return x * 10

numbers = [1, 2, 3, 4, 5]
multiplied_numbers = list(map(multiply_by_10, numbers))
print(multiplied_numbers)

# Example 7: Boolean conversion
def to_boolean(x):
    return bool(x)

values = [0, 1, '', 'hello']
booleans = list(map(to_boolean, values))
print(booleans)

# Example 8: Absolute value
def absolute(x):
    return abs(x)

numbers = [-1, -2, 3, -4, 5]
absolute_numbers = list(map(absolute, numbers))
print(absolute_numbers)

# Example 9: Strip whitespace
def strip_whitespace(s):
    return s.strip()

strings = ['  hello  ', '  world  ']
stripped_strings = list(map(strip_whitespace, strings))
print(stripped_strings)

# Example 10: Convert to float
def to_float(x):
    return float(x)

numbers = [1, 2, 3, 4, 5]
float_numbers = list(map(to_float, numbers))
print(float_numbers)

# Example 11: Check even
def is_even(x):
    return x % 2 == 0

numbers = [1, 2, 3, 4, 5]
even_check = list(map(is_even, numbers))
print(even_check)

# Example 12: Reverse strings
def reverse_string(s):
    return s[::-1]

strings = ['hello', 'world']
reversed_strings = list(map(reverse_string, strings))
print(reversed_strings)

# Example 13: Title case
def to_title(s):
    return s.title()

strings = ['hello world', 'python programming']
title_strings = list(map(to_title, strings))
print(title_strings)

# Example 14: Add prefix
def add_prefix(s):
    return 'prefix_' + s

strings = ['one', 'two', 'three']
prefixed_strings = list(map(add_prefix, strings))
print(prefixed_strings)

# Example 15: Add suffix
def add_suffix(s):
    return s + '_suffix'

strings = ['one', 'two', 'three']
suffixed_strings = list(map(add_suffix, strings))
print(suffixed_strings)

# Example 16: Convert to binary
def to_binary(x):
    return bin(x)

numbers = [1, 2, 3, 4, 5]
binary_numbers = list(map(to_binary, numbers))
print(binary_numbers)

# Example 17: Convert to hexadecimal
def to_hex(x):
    return hex(x)

numbers = [1, 2, 3, 4, 5]
hex_numbers = list(map(to_hex, numbers))
print(hex_numbers)

# Example 18: Convert to octal
def to_octal(x):
    return oct(x)

numbers = [1, 2, 3, 4, 5]
octal_numbers = list(map(to_octal, numbers))
print(octal_numbers)

# Example 19: Negate numbers
def negate(x):
    return -x

numbers = [1, 2, 3, 4, 5]
negated_numbers = list(map(negate, numbers))
print(negated_numbers)

# Example 20: Convert to boolean strings
def to_boolean_string(x):
    return str(bool(x))

values = [0, 1, '', 'hello']
boolean_strings = list(map(to_boolean_string, values))
print(boolean_strings)

# Example 21: Increment numbers
def increment(x):
    return x + 1

numbers = [1, 2, 3, 4, 5]
incremented_numbers = list(map(increment, numbers))
print(incremented_numbers)

# Example 22: Decrement numbers
def decrement(x):
    return x - 1

numbers = [1, 2, 3, 4, 5]
decremented_numbers = list(map(decrement, numbers))
print(decremented_numbers)

# Example 23: Convert to lowercase
def to_lowercase(s):
    return s.lower()

strings = ['HELLO', 'WORLD']
lowercase_strings = list(map(to_lowercase, strings))
print(lowercase_strings)

# Example 24: Repeat strings
def repeat_string(s):
    return s * 2

strings = ['hello', 'world']
repeated_strings = list(map(repeat_string, strings))
print(repeated_strings)

# Example 25: Check positive
def is_positive(x):
    return x > 0

numbers = [-1, 2, -3, 4, -5]
positive_check = list(map(is_positive, numbers))
print(positive_check)

# Example 26: Check negative
def is_negative(x):
    return x < 0

numbers = [-1, 2, -3, 4, -5]
negative_check = list(map(is_negative, numbers))
print(negative_check)

# Example 27: Convert to complex
def to_complex(x):
    return complex(x)

numbers = [1, 2, 3, 4, 5]
complex_numbers = list(map(to_complex, numbers))
print(complex_numbers)

# Example 28: Convert to list
def to_list(x):
    return list(x)

strings = ['hello', 'world']
list_strings = list(map(to_list, strings))
print(list_strings)

# Example 29: Convert to set
def to_set(x):
    return set(x)

strings = ['hello', 'world']
set_strings = list(map(to_set, strings))
print(set_strings)

# Example 30: Convert to tuple
def to_tuple(x):
    return tuple(x)

strings = ['hello', 'world']
tuple_strings = list(map(to_tuple, strings))
print(tuple_strings)