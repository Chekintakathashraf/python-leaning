# Example 1
a = [1, 2, 3]
b = [4, 5, 6]
print(list(zip(a, b)))  # [(1, 4), (2, 5), (3, 6)]

# Example 2
a = ['a', 'b', 'c']
b = [1, 2, 3]
print(list(zip(a, b)))  # [('a', 1), ('b', 2), ('c', 3)]

# Example 3
a = [1, 2, 3]
b = [4, 5, 6]
c = [7, 8, 9]
print(list(zip(a, b, c)))  # [(1, 4, 7), (2, 5, 8), (3, 6, 9)]

# Example 4
a = [1, 2]
b = [3, 4, 5]
print(list(zip(a, b)))  # [(1, 3), (2, 4)]

# Example 5
a = [1, 2, 3]
b = [4, 5]
print(list(zip(a, b)))  # [(1, 4), (2, 5)]

# Example 6
a = 'abc'
b = [1, 2, 3]
print(list(zip(a, b)))  # [('a', 1), ('b', 2), ('c', 3)]

# Example 7
a = [1, 2, 3]
b = (4, 5, 6)
print(list(zip(a, b)))  # [(1, 4), (2, 5), (3, 6)]

# Example 8
a = [1, 2, 3]
b = {4, 5, 6}
print(list(zip(a, b)))  # [(1, 4), (2, 5), (3, 6)]

# Example 9
a = [1, 2, 3]
b = {1: 'a', 2: 'b', 3: 'c'}
print(list(zip(a, b)))  # [(1, 1), (2, 2), (3, 3)]

# Example 10
a = [1, 2, 3]
b = {1: 'a', 2: 'b', 3: 'c'}
print(list(zip(a, b.values())))  # [(1, 'a'), (2, 'b'), (3, 'c')]

# Example 11
a = [1, 2, 3]
b = {1: 'a', 2: 'b', 3: 'c'}
print(list(zip(a, b.items())))  # [(1, (1, 'a')), (2, (2, 'b')), (3, (3, 'c'))]

# Example 12
a = [1, 2, 3]
b = [4, 5, 6]
c = [7, 8]
print(list(zip(a, b, c)))  # [(1, 4, 7), (2, 5, 8)]

# Example 13
a = [1, 2, 3]
b = [4, 5, 6]
c = [7]
print(list(zip(a, b, c)))  # [(1, 4, 7)]

# Example 14
a = [1, 2, 3]
b = [4, 5, 6]
c = []
print(list(zip(a, b, c)))  # []

# Example 15
a = [1, 2, 3]
b = [4, 5, 6]
print(dict(zip(a, b)))  # {1: 4, 2: 5, 3: 6}

# Example 16
a = ['a', 'b', 'c']
b = [1, 2, 3]
print(dict(zip(a, b)))  # {'a': 1, 'b': 2, 'c': 3}

# Example 17
a = [1, 2, 3]
b = [4, 5, 6]
print(tuple(zip(a, b)))  # ((1, 4), (2, 5), (3, 6))

# Example 18
a = [1, 2, 3]
b = [4, 5, 6]
print(set(zip(a, b)))  # {(1, 4), (2, 5), (3, 6)}

# Example 19
a = [1, 2, 3]
b = [4, 5, 6]
print(frozenset(zip(a, b)))  # frozenset({(1, 4), (2, 5), (3, 6)})

# Example 20
a = [1, 2, 3]
b = [4, 5, 6]
print(list(zip(a, b, range(3))))  # [(1, 4, 0), (2, 5, 1), (3, 6, 2)]

# Example 21
a = [1, 2, 3]
b = [4, 5, 6]
print(list(zip(a, b, range(2))))  # [(1, 4, 0), (2, 5, 1)]

# Example 22
a = [1, 2, 3]
b = [4, 5, 6]
print(list(zip(a, b, range(4))))  # [(1, 4, 0), (2, 5, 1), (3, 6, 2)]

# Example 23
a = [1, 2, 3]
b = [4, 5, 6]
print(list(zip(a, b, 'abc')))  # [(1, 4, 'a'), (2, 5, 'b'), (3, 6, 'c')]

# Example 24
a = [1, 2, 3]
b = [4, 5, 6]
print(list(zip(a, b, 'ab')))  # [(1, 4, 'a'), (2, 5, 'b')]

# Example 25
a = [1, 2, 3]
b = [4, 5, 6]
print(list(zip(a, b, 'abcd')))  # [(1, 4, 'a'), (2, 5, 'b'), (3, 6, 'c')]

# Example 26
a = [1, 2, 3]
b = [4, 5, 6]
print(list(zip(a, b, [7, 8, 9])))  # [(1, 4, 7), (2, 5, 8), (3, 6, 9)]

# Example 27
a = [1, 2, 3]
b = [4, 5, 6]
print(list(zip(a, b, [7, 8])))  # [(1, 4, 7), (2, 5, 8)]

# Example 28
a = [1, 2, 3]
b = [4, 5, 6]
print(list(zip(a, b, [7])))  # [(1, 4, 7)]

# Example 29
a = [1, 2, 3]
b = [4, 5, 6]
print(list(zip(a, b, [])))  # []

# Example 30
a = [1, 2, 3]
b = [4, 5, 6]
print(list(zip(a, b, [7, 8, 9, 10])))  # [(1, 4, 7), (2, 5, 8), (3, 6, 9)]

# Example 31
a = [1, 2, 3]
b = [4, 5, 6]
print(list(zip(a, b, [7, 8, 9], 'abc')))  # [(1, 4, 7, 'a'), (2, 5, 8, 'b'), (3, 6, 9, 'c')]

# Example 32
a = [1, 2, 3]
b = [4, 5, 6]
print(list(zip(a, b, [7, 8, 9], 'ab')))  # [(1, 4, 7, 'a'), (2, 5, 8, 'b')]

# Example 33
a = [1, 2, 3]
b = [4, 5, 6]
print(list(zip(a, b, [7, 8, 9], 'abcd')))  # [(1, 4, 7, 'a'), (2, 5, 8, 'b'), (3, 6, 9, 'c')]

# Example 34
a = [1, 2, 3]
b = [4, 5, 6]
print(list(zip(a, b, [7, 8, 9], range(3))))  # [(1, 4, 7, 0), (2, 5, 8, 1), (3, 6, 9, 2)]

# Example 35
a = [1, 2, 3]
b = [4, 5, 6]
print(list(zip(a, b, [7, 8, 9], range(2))))  # [(1, 4, 7, 0), (2, 5, 8, 1)]

# Example 36
a = [1, 2, 3]
b = [4, 5, 6]
print(list(zip(a, b, [7, 8, 9], range(4))))  # [(1, 4, 7, 0), (2, 5, 8, 1), (3, 6, 9, 2)]