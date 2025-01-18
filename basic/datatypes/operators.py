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



# Advanced examples of assignment operators with pre-increment, post-increment, pre-decrement, and post-decrement

# Pre-increment
f = 5
f = f + 1
print(f)  # 6

# Post-increment
g = 5
print(g)  # 5
g = g + 1

# Pre-decrement
h = 5
h = h - 1
print(h)  # 4

# Post-decrement
i = 5
print(i)  # 5
i = i - 1

# Using functions to simulate pre-increment and post-increment
def pre_increment(val):
    val += 1
    return val

def post_increment(val):
    original_val = val
    val += 1
    return original_val, val

def pre_decrement(val):
    val -= 1
    return val

def post_decrement(val):
    original_val = val
    val -= 1
    return original_val, val

# Pre-increment
j = 5
j = pre_increment(j)
print(j)  # 6

# Post-increment
k = 5
k, new_k = post_increment(k)
print(k)  # 5
print(new_k)  # 6

# Pre-decrement
l = 5
l = pre_decrement(l)
print(l)  # 4

# Post-decrement
m = 5
m, new_m = post_decrement(m)
print(m)  # 5
print(new_m)  # 4

# More complex examples
n = 10
n += 1  # Pre-increment
print(n)  # 11

o = 10
print(o)  # 10
o += 1  # Post-increment

p = 10
p -= 1  # Pre-decrement
print(p)  # 9

q = 10
print(q)  # 10
q -= 1  # Post-decrement

# Using loops with pre-increment and post-increment
r = 0
for _ in range(5):
    r += 1  # Pre-increment
print(r)  # 5

s = 0
for _ in range(5):
    print(s)  # Post-increment
    s += 1