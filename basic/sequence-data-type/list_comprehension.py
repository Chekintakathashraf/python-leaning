# List comprehension examples

# 1. Basic list comprehension
squares = [x**2 for x in range(10)]
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# 2. List comprehension with condition
evens = [x for x in range(10) if x % 2 == 0]
# [0, 2, 4, 6, 8]

# 3. Nested list comprehension
matrix = [[j for j in range(5)] for i in range(3)]
# [[0, 1, 2, 3, 4], [0, 1, 2, 3, 4], [0, 1, 2, 3, 4]]

# 4. List comprehension with function
def square(x):
    return x**2

squares_func = [square(x) for x in range(10)]
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# 5. List comprehension with multiple conditions
filtered = [x for x in range(20) if x % 2 == 0 if x % 3 == 0]
# [0, 6, 12, 18]

# 6. List comprehension with string
chars = [char for char in 'hello']
# ['h', 'e', 'l', 'l', 'o']

# 7. List comprehension with nested loops
pairs = [(x, y) for x in range(3) for y in range(3)]
# [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]

# 8. List comprehension with dictionary
dict_comp = {x: x**2 for x in range(5)}
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# 9. List comprehension with set
set_comp = {x for x in range(10) if x % 2 == 0}
# {0, 2, 4, 6, 8}

# 10. List comprehension with tuple
tuple_comp = tuple(x for x in range(5))
# (0, 1, 2, 3, 4)

# 11. List comprehension with list of lists
list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for sublist in list_of_lists for num in sublist]
# [1, 2, 3, 4, 5, 6, 7, 8, 9]

# 12. List comprehension with string methods
upper_chars = [char.upper() for char in 'hello']
# ['H', 'E', 'L', 'L', 'O']

# 13. List comprehension with enumerate
indexed_chars = [(i, char) for i, char in enumerate('hello')]
# [(0, 'h'), (1, 'e'), (2, 'l'), (3, 'l'), (4, 'o')]

# 14. List comprehension with zip
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
zipped = [(x, y) for x, y in zip(list1, list2)]
# [(1, 'a'), (2, 'b'), (3, 'c')]

# 15. List comprehension with range and step
stepped_range = [x for x in range(0, 10, 2)]
# [0, 2, 4, 6, 8]

# 16. List comprehension with filtering None values
values = [1, None, 2, None, 3]
filtered_values = [x for x in values if x is not None]
# [1, 2, 3]

# 17. List comprehension with type checking
mixed = [1, 'a', 2.5, 'b', 3]
integers = [x for x in mixed if isinstance(x, int)]
# [1, 3]

# 18. List comprehension with list slicing
sliced = [x for x in range(10)][::2]
# [0, 2, 4, 6, 8]

# 19. List comprehension with string splitting
sentence = "hello world"
words = [word for word in sentence.split()]
# ['hello', 'world']

# 20. List comprehension with string joining
joined = ''.join([char for char in 'hello'])
# 'hello'

# 21. List comprehension with list reversal
reversed_list = [x for x in reversed(range(5))]
# [4, 3, 2, 1, 0]

# 22. List comprehension with list of tuples
tuples = [(1, 2), (3, 4), (5, 6)]
flattened_tuples = [item for sublist in tuples for item in sublist]
# [1, 2, 3, 4, 5, 6]

# 23. List comprehension with list of dictionaries
list_of_dicts = [{'a': 1}, {'b': 2}, {'c': 3}]
keys = [key for d in list_of_dicts for key in d]
# ['a', 'b', 'c']

# 24. List comprehension with list of sets
list_of_sets = [{1, 2}, {3, 4}, {5, 6}]
flattened_sets = [item for s in list_of_sets for item in s]
# [1, 2, 3, 4, 5, 6]

# 25. List comprehension with list of strings
list_of_strings = ['hello', 'world']
flattened_strings = [char for string in list_of_strings for char in string]
# ['h', 'e', 'l', 'l', 'o', 'w', 'o', 'r', 'l', 'd']

# 26. List comprehension with list of tuples and condition
tuples_with_condition = [(x, y) for x in range(3) for y in range(3) if x != y]
# [(0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1)]

# 27. List comprehension with list of lists and condition
list_of_lists_with_condition = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
filtered_flattened = [num for sublist in list_of_lists_with_condition for num in sublist if num % 2 == 0]
# [2, 4, 6, 8]

# 28. List comprehension with list of dictionaries and condition
list_of_dicts_with_condition = [{'a': 1}, {'b': 2}, {'c': 3}]
filtered_keys = [key for d in list_of_dicts_with_condition for key in d if d[key] % 2 == 0]
# ['b']

# 29. List comprehension with list of sets and condition
list_of_sets_with_condition = [{1, 2}, {3, 4}, {5, 6}]
filtered_flattened_sets = [item for s in list_of_sets_with_condition for item in s if item % 2 == 0]
# [2, 4, 6]

# 30. List comprehension with list of strings and condition
list_of_strings_with_condition = ['hello', 'world']
filtered_flattened_strings = [char for string in list_of_strings_with_condition for char in string if char in 'aeiou']
# ['e', 'o', 'o']