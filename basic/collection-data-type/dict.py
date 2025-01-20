# Example 1: Creating a dictionary
my_dict = {'name': 'John', 'age': 25, 'city': 'New York'}

# Example 2: Accessing a value by key
print(my_dict['name'])  # Output: John

# Example 3: Adding a new key-value pair
my_dict['email'] = 'john@example.com'

# Example 4: Updating an existing value
my_dict['age'] = 26

# Example 5: Deleting a key-value pair
del my_dict['city']

# Example 6: Using the get() method
print(my_dict.get('name'))  # Output: John

# Example 7: Using the keys() method
print(my_dict.keys())  # Output: dict_keys(['name', 'age', 'email'])

# Example 8: Using the values() method
print(my_dict.values())  # Output: dict_values(['John', 26, 'john@example.com'])

# Example 9: Using the items() method
print(my_dict.items())  # Output: dict_items([('name', 'John'), ('age', 26), ('email', 'john@example.com')])

# Example 10: Looping through keys
for key in my_dict:
    print(key)

# Example 11: Looping through values
for value in my_dict.values():
    print(value)

# Example 12: Looping through key-value pairs
for key, value in my_dict.items():
    print(f"{key}: {value}")

# Example 13: Checking if a key exists
if 'name' in my_dict:
    print('Name is present')

# Example 14: Using the pop() method
my_dict.pop('email')

# Example 15: Using the popitem() method
my_dict.popitem()

# Example 16: Using the clear() method
my_dict.clear()

# Example 17: Using the copy() method
my_dict = {'name': 'John', 'age': 25}
new_dict = my_dict.copy()

# Example 18: Using the fromkeys() method
keys = ['name', 'age', 'city']
default_value = None
new_dict = dict.fromkeys(keys, default_value)

# Example 19: Using the setdefault() method
my_dict.setdefault('email', 'john@example.com')

# Example 20: Nested dictionary
nested_dict = {'person': {'name': 'John', 'age': 25}, 'address': {'city': 'New York', 'zip': '10001'}}

# Example 21: Accessing nested dictionary
print(nested_dict['person']['name'])  # Output: John

# Example 22: Updating nested dictionary
nested_dict['person']['age'] = 26

# Example 23: Adding to nested dictionary
nested_dict['address']['street'] = '5th Avenue'

# Example 24: Deleting from nested dictionary
del nested_dict['address']['zip']

# Example 25: Dictionary comprehension
squares = {x: x*x for x in range(6)}

# Example 26: Dictionary with mixed keys
mixed_dict = {1: 'apple', 'two': 2, (3, 4): 'tuple'}

# Example 27: Using the update() method
my_dict.update({'city': 'New York', 'email': 'john@example.com'})

# Example 28: Using the len() function
print(len(my_dict))  # Output: 4

# Example 29: Using the any() function
print(any(my_dict))  # Output: True

# Example 30: Using the all() function
print(all(my_dict))  # Output: True

# Example 31: Using the sorted() function
sorted_keys = sorted(my_dict)

# Example 32: Using the dict() constructor
new_dict = dict(name='John', age=25, city='New York')

# Example 33: Using the zip() function to create a dictionary
keys = ['name', 'age', 'city']
values = ['John', 25, 'New York']
zipped_dict = dict(zip(keys, values))

# Example 34: Using the enumerate() function
for index, key in enumerate(my_dict):
    print(index, key)

# Example 35: Using the max() function
max_key = max(my_dict)

# Example 36: Using the min() function
min_key = min(my_dict)

# Example 37: Using the sum() function
numeric_dict = {'a': 1, 'b': 2, 'c': 3}
total = sum(numeric_dict.values())

# Example 38: Using the dict() with keyword arguments
new_dict = dict(name='John', age=25)

# Example 39: Using the dict() with a list of tuples
tuple_list = [('name', 'John'), ('age', 25)]
new_dict = dict(tuple_list)

# Example 40: Using the dict() with a list of lists
list_list = [['name', 'John'], ['age', 25]]
new_dict = dict(list_list)

# Example 41: Using the dict() with a list of dictionaries
dict_list = [{'name': 'John'}, {'age': 25}]
new_dict = {k: v for d in dict_list for k, v in d.items()}

# Example 42: Using the dict() with a set of tuples
tuple_set = {('name', 'John'), ('age', 25)}
new_dict = dict(tuple_set)

# Example 43: Using the dict() with a set of lists
list_set = {('name', 'John'), ('age', 25)}
new_dict = dict(list_set)

# Example 44: Using the dict() with a set of dictionaries
dict_set = [{'name': 'John'}, {'age': 25}]
new_dict = {k: v for d in dict_set for k, v in d.items()}

# Example 48: Using the dict() with a generator expression
gen_expr = ((x, x*x) for x in range(6))
new_dict = dict(gen_expr)

# Example 49: Using the dict() with a dictionary comprehension
comp_dict = {x: x*x for x in range(6)}

# Example 50: Using the dict() with a dictionary comprehension and condition
comp_cond_dict = {x: x*x for x in range(6) if x % 2 == 0}