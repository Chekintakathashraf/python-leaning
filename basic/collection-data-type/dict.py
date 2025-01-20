from collections import defaultdict
from collections import OrderedDict
from collections import Counter
from collections import namedtuple
from collections import deque
from collections import ChainMap
from collections import UserDict
from collections import UserList
from collections import UserString

# Adding items to a dictionary
dict1 = {}
dict1['key1'] = 'value1'
dict1['key2'] = 'value2'
print(dict1)  # {'key1': 'value1', 'key2': 'value2'}

# Updating items in a dictionary
dict1['key1'] = 'new_value1'
print(dict1)  # {'key1': 'new_value1', 'key2': 'value2'}

# Clearing a dictionary
dict1.clear()
print(dict1)  # {}

# Copying a dictionary
dict2 = {'key1': 'value1', 'key2': 'value2'}
dict3 = dict2.copy()
print(dict3)  # {'key1': 'value1', 'key2': 'value2'}

# Looping through a dictionary
for key in dict2:
    print(key, dict2[key])  # key1 value1 \n key2 value2

# Dictionary comprehension
dict4 = {x: x**2 for x in range(5)}
print(dict4)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# Joining two dictionaries
dict5 = {'a': 1, 'b': 2}
dict6 = {'c': 3, 'd': 4}
dict7 = {**dict5, **dict6}
print(dict7)  # {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# Using the get method
value = dict2.get('key1')
print(value)  # value1

# Using the setdefault method
dict2.setdefault('key3', 'value3')
print(dict2)  # {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}

# Using the pop method
popped_value = dict2.pop('key1')
print(popped_value)  # value1
print(dict2)  # {'key2': 'value2', 'key3': 'value3'}

# Using the popitem method
popped_item = dict2.popitem()
print(popped_item)  # ('key3', 'value3')
print(dict2)  # {'key2': 'value2'}

# Using the keys method
keys = dict2.keys()
print(keys)  # dict_keys(['key2'])

# Using the values method
values = dict2.values()
print(values)  # dict_values(['value2'])

# Using the items method
items = dict2.items()
print(items)  # dict_items([('key2', 'value2')])

# Checking if a key exists in a dictionary
exists = 'key2' in dict2
print(exists)  # True

# Merging dictionaries using update method
dict8 = {'e': 5, 'f': 6}
dict5.update(dict8)
print(dict5)  # {'a': 1, 'b': 2, 'e': 5, 'f': 6}

# Creating a dictionary with fromkeys method
keys = ['a', 'b', 'c']
dict9 = dict.fromkeys(keys, 0)
print(dict9)  # {'a': 0, 'b': 0, 'c': 0}

# Nested dictionaries
nested_dict = {'dictA': {'key1': 'value1'}, 'dictB': {'key2': 'value2'}}
print(nested_dict)  # {'dictA': {'key1': 'value1'}, 'dictB': {'key2': 'value2'}}

# Accessing nested dictionary items
print(nested_dict['dictA']['key1'])  # value1

# Updating nested dictionary items
nested_dict['dictA']['key1'] = 'new_value1'
print(nested_dict)  # {'dictA': {'key1': 'new_value1'}, 'dictB': {'key2': 'value2'}}

# Deleting items from a dictionary
del dict2['key2']
print(dict2)  # {}

# Sorting dictionary by keys
sorted_by_keys = dict(sorted(dict2.items()))
print(sorted_by_keys)  # {'key2': 'value2', 'key3': 'value3'}

# Sorting dictionary by values
sorted_by_values = dict(sorted(dict2.items(), key=lambda item: item[1]))
print(sorted_by_values)  # {'key2': 'value2', 'key3': 'value3'}

# Sorting dictionary by keys in reverse order
sorted_by_keys_reverse = dict(sorted(dict2.items(), reverse=True))
print(sorted_by_keys_reverse)  # {'key3': 'value3', 'key2': 'value2'}

# Sorting dictionary by values in reverse order
sorted_by_values_reverse = dict(sorted(dict2.items(), key=lambda item: item[1], reverse=True))
print(sorted_by_values_reverse)  # {'key3': 'value3', 'key2': 'value2'}

# Sorting dictionary by length of keys
sorted_by_key_length = dict(sorted(dict2.items(), key=lambda item: len(item[0])))
print(sorted_by_key_length)  # {'key2': 'value2', 'key3': 'value3'}

# Sorting dictionary by length of values
sorted_by_value_length = dict(sorted(dict2.items(), key=lambda item: len(item[1])))
print(sorted_by_value_length)  # {'key2': 'value2', 'key3': 'value3'}

# Dictionary with tuple keys
tuple_key_dict = {(1, 2): 'value1', (3, 4): 'value2'}
print(tuple_key_dict)  # {(1, 2): 'value1', (3, 4): 'value2'}

# Dictionary with list values
list_value_dict = {'key1': [1, 2, 3], 'key2': [4, 5, 6]}
print(list_value_dict)  # {'key1': [1, 2, 3], 'key2': [4, 5, 6]}

# Dictionary with mixed data types
mixed_dict = {'key1': 1, 'key2': 'value2', 'key3': [1, 2, 3]}
print(mixed_dict)  # {'key1': 1, 'key2': 'value2', 'key3': [1, 2, 3]}

# Dictionary with boolean values
bool_dict = {'key1': True, 'key2': False}
print(bool_dict)  # {'key1': True, 'key2': False}

# Dictionary with None values
none_dict = {'key1': None, 'key2': 'value2'}
print(none_dict)  # {'key1': None, 'key2': 'value2'}

# Dictionary with function values
def my_func():
    return 'Hello, World!'

func_dict = {'key1': my_func}
print(func_dict['key1']())  # Hello, World!

# Dictionary with lambda function values
lambda_dict = {'key1': lambda x: x * 2}
print(lambda_dict['key1'](5))  # 10

# Dictionary with class instances
class MyClass:
    def __init__(self, value):
        self.value = value

instance_dict = {'key1': MyClass(10)}
print(instance_dict['key1'].value)  # 10

# Dictionary with default values using defaultdict
default_dict = defaultdict(int)
default_dict['key1'] += 1
print(default_dict)  # defaultdict(<class 'int'>, {'key1': 1})

# Dictionary with ordered keys using OrderedDict
ordered_dict = OrderedDict()
ordered_dict['key1'] = 'value1'
ordered_dict['key2'] = 'value2'
print(ordered_dict)  # OrderedDict([('key1', 'value1'), ('key2', 'value2')])

# Dictionary with counter using Counter
counter_dict = Counter(['a', 'b', 'c', 'a', 'b', 'a'])
print(counter_dict)  # Counter({'a': 3, 'b': 2, 'c': 1})

# Dictionary with namedtuple values
Person = namedtuple('Person', 'name age')
namedtuple_dict = {'person1': Person('Alice', 30), 'person2': Person('Bob', 25)}
print(namedtuple_dict)  # {'person1': Person(name='Alice', age=30), 'person2': Person(name='Bob', age=25)}

# Dictionary with deque values
deque_dict = {'key1': deque([1, 2, 3])}
print(deque_dict)  # {'key1': deque([1, 2, 3])}

# Dictionary with ChainMap
dict10 = {'key1': 'value1'}
dict11 = {'key2': 'value2'}
chainmap_dict = ChainMap(dict10, dict11)
print(chainmap_dict)  # ChainMap({'key1': 'value1'}, {'key2': 'value2'})

# Dictionary with UserDict
class MyDict(UserDict):
    def __setitem__(self, key, value):
        super().__setitem__(key, value * 2)

user_dict = MyDict()
user_dict['key1'] = 10
print(user_dict)  # {'key1': 20}

# Dictionary with UserList
class MyList(UserList):
    def append(self, item):
        super().append(item * 2)

user_list_dict = {'key1': MyList([1, 2, 3])}
user_list_dict['key1'].append(4)
print(user_list_dict)  # {'key1': [1, 2, 3, 8]}

# Dictionary with UserString
class MyString(UserString):
    def __add__(self, other):
        return MyString(super().__add__(other).upper())

user_string_dict = {'key1': MyString('hello')}
user_string_dict['key1'] += ' world'
print(user_string_dict)  # {'key1': 'HELLO WORLD'}

# Dictionary with frozenset keys
frozenset_key_dict = {frozenset([1, 2, 3]): 'value1'}
print(frozenset_key_dict)  # {frozenset({1, 2, 3}): 'value1'}

# Dictionary with complex keys
complex_key_dict = {complex(1, 2): 'value1'}
print(complex_key_dict)  # {(1+2j): 'value1'}

# Dictionary with bytes keys
bytes_key_dict = {b'key1': 'value1'}
print(bytes_key_dict)  # {b'key1': 'value1'}

# Dictionary with bytearray keys
bytearray_key_dict = {bytearray(b'key1'): 'value1'}
print(bytearray_key_dict)  # {bytearray(b'key1'): 'value1'}

# Dictionary with memoryview keys
memoryview_key_dict = {memoryview(b'key1'): 'value1'}
print(memoryview_key_dict)  # {<memory at 0x7f8c8c8c8c40>: 'value1'}

# Dictionary with range keys
range_key_dict = {range(5): 'value1'}
print(range_key_dict)  # {range(0, 5): 'value1'}

# Dictionary with slice keys
slice_key_dict = {slice(1, 5): 'value1'}
print(slice_key_dict)  # {slice(1, 5, None): 'value1'}

# Dictionary with Ellipsis keys
ellipsis_key_dict = {Ellipsis: 'value1'}
print(ellipsis_key_dict)  # {Ellipsis: 'value1'}

# Dictionary with NotImplemented keys
not_implemented_key_dict = {NotImplemented: 'value1'}
print(not_implemented_key_dict)  # {NotImplemented: 'value1'}

# Dictionary with None keys
none_key_dict = {None: 'value1'}
print(none_key_dict)  # {None: 'value1'}

# Dictionary with boolean keys
boolean_key_dict = {True: 'value1', False: 'value2'}
print(boolean_key_dict)  # {True: 'value1', False: 'value2'}

# Dictionary with integer keys
integer_key_dict = {1: 'value1', 2: 'value2'}
print(integer_key_dict)  # {1: 'value1', 2: 'value2'}

# Dictionary with float keys
float_key_dict = {1.1: 'value1', 2.2: 'value2'}
print(float_key_dict)  # {1.1: 'value1', 2.2: 'value2'}

# Dictionary with string keys
string_key_dict = {'key1': 'value1', 'key2': 'value2'}
print(string_key_dict)  # {'key1': 'value1', 'key2': 'value2'}

# Dictionary with list keys (not allowed, will raise TypeError)
# list_key_dict = {[1, 2, 3]: 'value1'}  # TypeError: unhashable type: 'list'

# Dictionary with set keys (not allowed, will raise TypeError)
# set_key_dict = {set([1, 2, 3]): 'value1'}  # TypeError: unhashable type: 'set'

# Dictionary with dictionary keys (not allowed, will raise TypeError)
# dict_key_dict = {{'key1': 'value1'}: 'value2'}  # TypeError: unhashable type: 'dict'

# Dictionary with custom object keys
class CustomKey:
    def __init__(self, value):
        self.value = value

    def __hash__(self):
        return hash(self.value)

    def __eq__(self, other):
        return self.value == other.value

custom_key_dict = {CustomKey(1): 'value1'}
print(custom_key_dict)  # {<__main__.CustomKey object at 0x7f8c8c8c8c40>: 'value1'}

# Dictionary with custom object values
class CustomValue:
    def __init__(self, value):
        self.value = value

custom_value_dict = {'key1': CustomValue(1)}
print(custom_value_dict['key1'].value)  # 1

# Dictionary with custom object keys and values
custom_key_value_dict = {CustomKey(1): CustomValue(1)}
print(custom_key_value_dict[CustomKey(1)].value)  # 1

# Dictionary with custom object keys and values using __repr__
class CustomKeyRepr:
    def __init__(self, value):
        self.value = value

    def __hash__(self):
        return hash(self.value)

    def __eq__(self, other):
        return self.value == other.value

    def __repr__(self):
        return f'CustomKeyRepr({self.value})'

class CustomValueRepr:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f'CustomValueRepr({self.value})'

custom_key_value_repr_dict = {CustomKeyRepr(1): CustomValueRepr(1)}
print(custom_key_value_repr_dict)  # {CustomKeyRepr(1): CustomValueRepr(1)}

# Dictionary with custom object keys and values using __str__
class CustomKeyStr:
    def __init__(self, value):
        self.value = value

    def __hash__(self):
        return hash(self.value)

    def __eq__(self, other):
        return self.value == other.value

    def __str__(self):
        return f'CustomKeyStr({self.value})'

class CustomValueStr:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f'CustomValueStr({self.value})'

custom_key_value_str_dict = {CustomKeyStr(1): CustomValueStr(1)}
print(custom_key_value_str_dict)  # {CustomKeyStr(1): CustomValueStr(1)}

# Dictionary with custom object keys and values using __repr__ and __str__
class CustomKeyReprStr:
    def __init__(self, value):
        self.value = value

    def __hash__(self):
        return hash(self.value)

    def __eq__(self, other):
        return self.value == other.value

    def __repr__(self):
        return f'CustomKeyReprStr({self.value})'

    def __str__(self):
        return f'CustomKeyReprStr({self.value})'

class CustomValueReprStr:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f'CustomValueReprStr({self.value})'

    def __str__(self):
        return f'CustomValueReprStr({self.value})'

custom_key_value_repr_str_dict = {CustomKeyReprStr(1): CustomValueReprStr(1)}
print(custom_key_value_repr_str_dict)  # {CustomKeyReprStr(1): CustomValueReprStr(1)}