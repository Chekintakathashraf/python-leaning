# abs(x) - Returns the absolute value of a number
print(abs(-5))  # Output: 5

# all(iterable) - Returns True if all elements of the iterable are true
print(all([True, True, False]))  # Output: False

# any(iterable) - Returns True if any element of the iterable is true
print(any([False, False, True]))  # Output: True

# bin(x) - Converts an integer to a binary string
print(bin(10))  # Output: '0b1010'

# bool(x) - Converts a value to a Boolean
print(bool(0))  # Output: False

# chr(x) - Returns the string representing a character whose Unicode code point is the integer x
print(chr(97))  # Output: 'a'

# dir([object]) - Returns a list of the attributes and methods of any object
print(dir([]))  # Output: List of methods and attributes of a list

# divmod(a, b) - Returns a tuple containing the quotient and remainder when dividing a by b
print(divmod(10, 3))  # Output: (3, 1)

# enumerate(iterable, start=0) - Returns an enumerate object
for index, value in enumerate(['a', 'b', 'c']):
    print(index, value)  # Output: 0 a, 1 b, 2 c

# eval(expression) - Parses the expression passed to it and runs Python expression (code) within the program
print(eval('2 + 2'))  # Output: 4

# float(x) - Converts a number or a string to a floating point number
print(float('3.14'))  # Output: 3.14

# int(x) - Converts a number or a string to an integer
print(int('10'))  # Output: 10

# len(s) - Returns the length (the number of items) of an object
print(len('hello'))  # Output: 5

# max(iterable) - Returns the largest item in an iterable
print(max([1, 2, 3]))  # Output: 3

# min(iterable) - Returns the smallest item in an iterable
print(min([1, 2, 3]))  # Output: 1

# open(file, mode) - Opens a file and returns a corresponding file object
file = open('example.txt', 'w')
file.write('Hello, world!')
file.close()

# pow(x, y) - Returns x raised to the power y
print(pow(2, 3))  # Output: 8

# range(start, stop[, step]) - Returns an immutable sequence of numbers from start to stop by step
print(list(range(1, 10, 2)))  # Output: [1, 3, 5, 7, 9]

# round(number[, ndigits]) - Rounds a number to a specified number of decimal places
print(round(3.14159, 2))  # Output: 3.14

# sorted(iterable) - Returns a new sorted list from the elements of any iterable
print(sorted([3, 1, 2]))  # Output: [1, 2, 3]

# str(object) - Returns a string version of an object
print(str(123))  # Output: '123'

# sum(iterable) - Sums the items of an iterable
print(sum([1, 2, 3]))  # Output: 6

# type(object) - Returns the type of an object
print(type(123))  # Output: <class 'int'>