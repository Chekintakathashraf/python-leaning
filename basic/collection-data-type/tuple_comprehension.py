import math

# Tuple comprehensions are not directly supported in Python. 
# Instead, you can use a generator expression and convert it to a tuple.

# Example 1: Tuple of squares of numbers from 0 to 9
tuple1 = tuple(x**2 for x in range(10))
# (0, 1, 4, 9, 16, 25, 36, 49, 64, 81)

# Example 2: Tuple of even numbers from 0 to 19
tuple2 = tuple(x for x in range(20) if x % 2 == 0)
# (0, 2, 4, 6, 8, 10, 12, 14, 16, 18)

# Example 3: Tuple of lengths of words in a list
words = ["apple", "banana", "cherry"]
tuple3 = tuple(len(word) for word in words)
# (5, 6, 6)

# Example 4: Tuple of uppercase letters from a string
string = "hello"
tuple4 = tuple(char.upper() for char in string)
# ('H', 'E', 'L', 'L', 'O')

# Example 5: Tuple of first characters of words in a list
words = ["apple", "banana", "cherry"]
tuple5 = tuple(word[0] for word in words)
# ('a', 'b', 'c')

# Example 6: Tuple of numbers divisible by 3 from 0 to 29
tuple6 = tuple(x for x in range(30) if x % 3 == 0)
# (0, 3, 6, 9, 12, 15, 18, 21, 24, 27)

# Example 7: Tuple of tuples containing number and its square
tuple7 = tuple((x, x**2) for x in range(10))
# ((0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25), (6, 36), (7, 49), (8, 64), (9, 81))

# Example 8: Tuple of boolean values indicating if numbers are even
tuple8 = tuple(x % 2 == 0 for x in range(10))
# (True, False, True, False, True, False, True, False, True, False)

# Example 9: Tuple of reversed words
words = ["apple", "banana", "cherry"]
tuple9 = tuple(word[::-1] for word in words)
# ('elppa', 'ananab', 'yrrehc')

# Example 10: Tuple of ASCII values of characters in a string
string = "hello"
tuple10 = tuple(ord(char) for char in string)
# (104, 101, 108, 108, 111)

# Example 11: Tuple of numbers from 0 to 9 multiplied by 2
tuple11 = tuple(x * 2 for x in range(10))
# (0, 2, 4, 6, 8, 10, 12, 14, 16, 18)

# Example 12: Tuple of tuples containing number and its cube
tuple12 = tuple((x, x**3) for x in range(10))
# ((0, 0), (1, 1), (2, 8), (3, 27), (4, 64), (5, 125), (6, 216), (7, 343), (8, 512), (9, 729))

# Example 13: Tuple of numbers from 0 to 9 as strings
tuple13 = tuple(str(x) for x in range(10))
# ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')

# Example 14: Tuple of tuples containing word and its length
words = ["apple", "banana", "cherry"]
tuple14 = tuple((word, len(word)) for word in words)
# (('apple', 5), ('banana', 6), ('cherry', 6))

# Example 15: Tuple of numbers from 0 to 9 with 1 added to each
tuple15 = tuple(x + 1 for x in range(10))
# (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

# Example 16: Tuple of tuples containing number and its factorial
tuple16 = tuple((x, math.factorial(x)) for x in range(10))
# ((0, 1), (1, 1), (2, 2), (3, 6), (4, 24), (5, 120), (6, 720), (7, 5040), (8, 40320), (9, 362880))

# Example 17: Tuple of numbers from 0 to 9 as floats
tuple17 = tuple(float(x) for x in range(10))
# (0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0)

# Example 18: Tuple of tuples containing number and its binary representation
tuple18 = tuple((x, bin(x)) for x in range(10))
# ((0, '0b0'), (1, '0b1'), (2, '0b10'), (3, '0b11'), (4, '0b100'), (5, '0b101'), (6, '0b110'), (7, '0b111'), (8, '0b1000'), (9, '0b1001'))

# Example 19: Tuple of numbers from 0 to 9 with 5 subtracted from each
tuple19 = tuple(x - 5 for x in range(10))
# (-5, -4, -3, -2, -1, 0, 1, 2, 3, 4)

# Example 20: Tuple of tuples containing number and its hexadecimal representation
tuple20 = tuple((x, hex(x)) for x in range(10))
# ((0, '0x0'), (1, '0x1'), (2, '0x2'), (3, '0x3'), (4, '0x4'), (5, '0x5'), (6, '0x6'), (7, '0x7'), (8, '0x8'), (9, '0x9'))

# Example 21: Tuple of numbers from 0 to 9 divided by 2
tuple21 = tuple(x / 2 for x in range(10))
# (0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5)

# Example 22: Tuple of tuples containing number and its octal representation
tuple22 = tuple((x, oct(x)) for x in range(10))
# ((0, '0o0'), (1, '0o1'), (2, '0o2'), (3, '0o3'), (4, '0o4'), (5, '0o5'), (6, '0o6'), (7, '0o7'), (8, '0o10'), (9, '0o11'))

# Example 23: Tuple of numbers from 0 to 9 with each multiplied by itself
tuple23 = tuple(x * x for x in range(10))
# (0, 1, 4, 9, 16, 25, 36, 49, 64, 81)

# Example 24: Tuple of tuples containing number and its square root
tuple24 = tuple((x, math.sqrt(x)) for x in range(10))
# ((0, 0.0), (1, 1.0), (2, 1.4142135623730951), (3, 1.7320508075688772), (4, 2.0), (5, 2.23606797749979), (6, 2.449489742783178), (7, 2.6457513110645907), (8, 2.8284271247461903), (9, 3.0))

# Example 25: Tuple of numbers from 0 to 9 with each raised to the power of 3
tuple25 = tuple(x ** 3 for x in range(10))
# (0, 1, 8, 27, 64, 125, 216, 343, 512, 729)

# Example 26: Tuple of tuples containing number and its natural logarithm
tuple26 = tuple((x, math.log(x + 1)) for x in range(10))
# ((0, 0.0), (1, 0.6931471805599453), (2, 1.0986122886681098), (3, 1.3862943611198906), (4, 1.6094379124341003), (5, 1.791759469228055), (6, 1.9459101490553132), (7, 2.0794415416798357), (8, 2.1972245773362196), (9, 2.302585092994046))

# Example 27: Tuple of numbers from 0 to 9 with each raised to the power of 4
tuple27 = tuple(x ** 4 for x in range(10))
# (0, 1, 16, 81, 256, 625, 1296, 2401, 4096, 6561)

# Example 28: Tuple of tuples containing number and its sine value
tuple28 = tuple((x, math.sin(x)) for x in range(10))
# ((0, 0.0), (1, 0.8414709848078965), (2, 0.9092974268256817), (3, 0.1411200080598672), (4, -0.7568024953079282), (5, -0.9589242746631385), (6, -0.27941549819892586), (7, 0.6569865987187891), (8, 0.9893582466233818), (9, 0.4121184852417566))

# Example 29: Tuple of numbers from 0 to 9 with each raised to the power of 5
tuple29 = tuple(x ** 5 for x in range(10))
# (0, 1, 32, 243, 1024, 3125, 7776, 16807, 32768, 59049)

# Example 30: Tuple of tuples containing number and its cosine value
tuple30 = tuple((x, math.cos(x)) for x in range(10))
# ((0, 1.0), (1, 0.5403023058681398), (2, -0.4161468365471424), (3, -0.9899924966004454), (4, -0.6536436208636119), (5, 0.28366218546322625), (6, 0.960170286650366), (7, 0.7539022543433046), (8, -0.14550003380861354), (9, -0.9111302618846769))