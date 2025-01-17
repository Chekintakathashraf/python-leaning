# Slicing examples in Python

# Basic slicing
a = [1, 2, 3, 4, 5]
print(a[1:4])  # [2, 3, 4]

# Slicing with step
print(a[0:5:2])  # [1, 3, 5]

# Slicing with negative step
print(a[::-1])  # [5, 4, 3, 2, 1]

# Slicing with negative indices
print(a[-4:-1])  # [2, 3, 4]

# Slicing with negative step and negative indices
print(a[-1:-6:-1])  # [5, 4, 3, 2, 1]

# Slicing with omitted start
print(a[:3])  # [1, 2, 3]

# Slicing with omitted end
print(a[2:])  # [3, 4, 5]

# Slicing with omitted start and end
print(a[:])  # [1, 2, 3, 4, 5]

# Slicing with omitted start and step
print(a[::2])  # [1, 3, 5]

# Slicing with omitted end and step
print(a[1::2])  # [2, 4]

# Slicing with negative step and omitted start
print(a[::-2])  # [5, 3, 1]

# Slicing with negative step and omitted end
print(a[4::-2])  # [5, 3, 1]

# Slicing with negative step, omitted start and end
print(a[::-1])  # [5, 4, 3, 2, 1]

# Slicing strings
s = "Hello, World!"
print(s[7:12])  # 'World'

# Slicing strings with step
print(s[::2])  # 'Hlo ol!'

# Slicing strings with negative step
print(s[::-1])  # '!dlroW ,olleH'

# Slicing strings with negative indices
print(s[-6:-1])  # 'World'

# Slicing strings with negative step and negative indices
print(s[-1:-6:-1])  # '!dlro'

# Slicing tuples
t = (1, 2, 3, 4, 5)
print(t[1:4])  # (2, 3, 4)

# Slicing tuples with step
print(t[0:5:2])  # (1, 3, 5)

# Slicing tuples with negative step
print(t[::-1])  # (5, 4, 3, 2, 1)

# Slicing tuples with negative indices
print(t[-4:-1])  # (2, 3, 4)

# Slicing tuples with negative step and negative indices
print(t[-1:-6:-1])  # (5, 4, 3, 2, 1)

# Slicing with step greater than length
print(a[::10])  # [1]

# Slicing with negative step greater than length
print(a[::-10])  # [5]

# Slicing with step of 1
print(a[::1])  # [1, 2, 3, 4, 5]

# Slicing with negative step of -1
print(a[::-1])  # [5, 4, 3, 2, 1]

# Slicing with step of 0 (invalid)
# print(a[::0])  # ValueError: slice step cannot be zero

# Slicing with start greater than end
print(a[4:1])  # []

# Slicing with start equal to end
print(a[2:2])  # []

# Slicing with start less than end
print(a[1:4])  # [2, 3, 4]