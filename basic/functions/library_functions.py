# Example of some common Python library functions:

# 1. abs(x)
# Returns the absolute value of a number.
print(abs(-5))  # Output: 5

# 2. all(iterable)
# Returns True if all elements of the iterable are true (or if the iterable is empty).
print(all([True, True, False]))  # Output: False

# 3. any(iterable)
# Returns True if any element of the iterable is true. If the iterable is empty, returns False.
print(any([False, False, True]))  # Output: True

# 4. bin(x)
# Converts an integer number to a binary string prefixed with “0b”.
print(bin(10))  # Output: '0b1010'

# 5. bool(x)
# Converts a value to a Boolean, using the standard truth testing procedure.
print(bool(0))  # Output: False

# 6. chr(i)
# Returns the string representing a character whose Unicode code point is the integer i.
print(chr(97))  # Output: 'a'

# 7. divmod(a, b)
# Takes two numbers and returns a pair of numbers (a // b, a % b).
print(divmod(9, 2))  # Output: (4, 1)

# 8. enumerate(iterable, start=0)
# Returns an enumerate object. It contains pairs of index and value from the iterable.
for index, value in enumerate(['a', 'b', 'c']):
    print(index, value)  # Output: 0 a, 1 b, 2 c

# 9. filter(function, iterable)
# Constructs an iterator from elements of iterable for which function returns true.
print(list(filter(lambda x: x > 0, [-1, 0, 1, 2])))  # Output: [1, 2]

# 10. float(x)
# Converts a number or a string to a floating point number.
print(float('3.14'))  # Output: 3.14

# 11. int(x)
# Converts a number or string to an integer.
print(int('10'))  # Output: 10

# 12. len(s)
# Returns the length (the number of items) of an object.
print(len([1, 2, 3]))  # Output: 3

# 13. map(function, iterable)
# Applies function to every item of iterable and returns a list of the results.
print(list(map(lambda x: x * 2, [1, 2, 3])))  # Output: [2, 4, 6]

# 14. max(iterable)
# Returns the largest item in an iterable or the largest of two or more arguments.
print(max([1, 2, 3]))  # Output: 3

# 15. min(iterable)
# Returns the smallest item in an iterable or the smallest of two or more arguments.
print(min([1, 2, 3]))  # Output: 1

# 16. pow(x, y)
# Returns x raised to the power y.
print(pow(2, 3))  # Output: 8

# 17. range(start, stop, step)
# Generates a sequence of numbers from start to stop by step.
print(list(range(1, 10, 2)))  # Output: [1, 3, 5, 7, 9]

# 18. round(number, ndigits)
# Rounds a number to a given precision in decimal digits.
print(round(3.14159, 2))  # Output: 3.14

# 19. sorted(iterable)
# Returns a new sorted list from the items in iterable.
print(sorted([3, 1, 2]))  # Output: [1, 2, 3]

# 20. sum(iterable)
# Sums start and the items of an iterable from left to right and returns the total.
print(sum([1, 2, 3]))  # Output: 6

# 21. type(object)
# Returns the type of an object.
print(type(123))  # Output: <class 'int'>