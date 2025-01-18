# Arithmetic Operators
a = 10
b = 3
print(a + b)  # Addition: 13
print(a - b)  # Subtraction: 7
print(a * b)  # Multiplication: 30
print(a / b)  # Division: 3.333...
print(a % b)  # Modulus: 1
print(a ** b) # Exponentiation: 1000
print(a // b) # Floor Division: 3

# String concatenation using arithmetic operator
str1 = "Hello"
str2 = "World"
print(str1 + " " + str2)  # Concatenation: Hello World

# Comparison Operators
print(a == b)  # Equal: False
print(a != b)  # Not equal: True
print(a > b)   # Greater than: True
print(a < b)   # Less than: False
print(a >= b)  # Greater than or equal to: True
print(a <= b)  # Less than or equal to: False

# Boolean comparison
bool1 = True
bool2 = False
print(bool1 == bool2)  # Equal: False
print(bool1 != bool2)  # Not equal: True

# Assignment Operators
c = 5
c += 2  # c = c + 2: 7
c -= 2  # c = c - 2: 5
c *= 2  # c = c * 2: 10
c /= 2  # c = c / 2: 5.0
c %= 3  # c = c % 3: 2.0
c **= 2 # c = c ** 2: 4.0
c //= 2 # c = c // 2: 2.0

# Logical Operators
print(bool1 and bool2)  # Logical AND: False
print(bool1 or bool2)   # Logical OR: True
print(not bool1)        # Logical NOT: False

# Bitwise Operators
x = 5  # 0101 in binary
y = 3  # 0011 in binary
print(x & y)  # Bitwise AND: 1 (0001 in binary)
print(x | y)  # Bitwise OR: 7 (0111 in binary)
print(x ^ y)  # Bitwise XOR: 6 (0110 in binary)
print(~x)     # Bitwise NOT: -6 (inverts all bits)
print(x << 1) # Bitwise left shift: 10 (1010 in binary)
print(x >> 1) # Bitwise right shift: 2 (0010 in binary)

# Membership Operators
list1 = [1, 2, 3, 4, 5]
print(3 in list1)   # in: True
print(6 not in list1) # not in: True

# Identity Operators
d = 10
e = 10
print(d is e)  # is: True (both refer to the same object)
print(d is not e)  # is not: False (both refer to the same object)

# String identity
str3 = "Hello"
str4 = "Hello"
print(str3 is str4)  # is: True (both refer to the same object)
print(str3 is not str4)  # is not: False (both refer to the same object)