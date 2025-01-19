import math
import traceback
import datetime
from decimal import Decimal
from fractions import Fraction
import uuid
from collections import namedtuple
from collections import deque
from collections import Counter
from collections import OrderedDict
from collections import defaultdict
from collections import ChainMap
from collections import UserDict
from collections import UserList
from collections import UserString

# Tuples in Python

# Creating tuples
empty_tuple = ()
single_element_tuple = (1,)
multiple_elements_tuple = (1, 2, 3, 4, 5)
mixed_tuple = (1, "Hello", 3.14, True)

# Accessing elements
first_element = multiple_elements_tuple[0]  # 1
last_element = multiple_elements_tuple[-1]  # 5

# Slicing tuples
slice_tuple = multiple_elements_tuple[1:3]  # (2, 3)

# Looping through tuples
for element in multiple_elements_tuple:
    print(element)

# Tuple methods
count_of_1 = multiple_elements_tuple.count(1)  # 1
index_of_3 = multiple_elements_tuple.index(3)  # 2

# Tuple concatenation
concatenated_tuple = multiple_elements_tuple + mixed_tuple

# Tuple repetition
repeated_tuple = single_element_tuple * 3  # (1, 1, 1)

# Tuple unpacking
a, b, c, d, e = multiple_elements_tuple

# Using asterisk for unpacking
first, *middle, last = multiple_elements_tuple

# Nested tuples
nested_tuple = (1, (2, 3), (4, 5, 6))

# Tuple comprehension (using generator expression)
tuple_comprehension = tuple(x * 2 for x in range(5))  # (0, 2, 4, 6, 8)

# Joining tuples
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
joined_tuple = tuple1 + tuple2

# Packing and unpacking
packed_tuple = 1, 2, 3  # Packing
x, y, z = packed_tuple  # Unpacking

# Tuple with different data types
mixed_data_tuple = (1, "apple", 3.14, [1, 2, 3], {"key": "value"})

# Tuple immutability
# multiple_elements_tuple[0] = 10  # This will raise a TypeError

# Tuple with functions
def return_multiple_values():
    return 1, 2, 3

result_tuple = return_multiple_values()

# Tuple with a single element (note the comma)
single_element = (42,)

# Tuple with no parentheses
no_parentheses_tuple = 1, 2, 3

# Tuple with list inside
tuple_with_list = (1, [2, 3], 4)

# Tuple with dictionary inside
tuple_with_dict = (1, {"key": "value"}, 3)

# Tuple with set inside
tuple_with_set = (1, {2, 3}, 4)

# Tuple with another tuple inside
tuple_with_tuple = (1, (2, 3), 4)

# Tuple with boolean values
boolean_tuple = (True, False, True)

# Tuple with None value
none_tuple = (None, 1, 2)

# Tuple with complex numbers
complex_tuple = (1 + 2j, 3 + 4j)

# Tuple with bytes
bytes_tuple = (b'hello', b'world')

# Tuple with bytearray
bytearray_tuple = (bytearray(b'hello'), bytearray(b'world'))

# Tuple with memoryview
memoryview_tuple = (memoryview(b'hello'), memoryview(b'world'))

# Tuple with range
range_tuple = (range(5), range(10))

# Tuple with frozenset
frozenset_tuple = (frozenset([1, 2, 3]), frozenset([4, 5, 6]))

# Tuple with slice
slice_tuple = (slice(5), slice(10))

# Tuple with Ellipsis
ellipsis_tuple = (Ellipsis, 1, 2)

# Tuple with NotImplemented
not_implemented_tuple = (NotImplemented, 1, 2)

# Tuple with class
class MyClass:
    pass

class_tuple = (MyClass(), MyClass())

# Tuple with function
def my_function():
    pass

function_tuple = (my_function, my_function)

# Tuple with lambda
lambda_tuple = (lambda x: x * 2, lambda x: x * 3)

# Tuple with module
module_tuple = (math, math)

# Tuple with exception
exception_tuple = (Exception("error"), ValueError("value error"))

# Tuple with traceback
try:
    1 / 0
except ZeroDivisionError as e:
    traceback_tuple = (traceback.format_exc(), e)

# Tuple with datetime
datetime_tuple = (datetime.datetime.now(), datetime.datetime.utcnow())

# Tuple with decimal
decimal_tuple = (Decimal('1.1'), Decimal('2.2'))

# Tuple with fractions
fraction_tuple = (Fraction(1, 2), Fraction(3, 4))

# Tuple with uuid
uuid_tuple = (uuid.uuid4(), uuid.uuid4())

# Tuple with namedtuple
Point = namedtuple('Point', ['x', 'y'])
namedtuple_tuple = (Point(1, 2), Point(3, 4))

# Tuple with deque
deque_tuple = (deque([1, 2, 3]), deque([4, 5, 6]))

# Tuple with Counter
counter_tuple = (Counter([1, 2, 3]), Counter([4, 5, 6]))

# Tuple with OrderedDict
ordered_dict_tuple = (OrderedDict([('a', 1), ('b', 2)]), OrderedDict([('c', 3), ('d', 4)]))

# Tuple with defaultdict
defaultdict_tuple = (defaultdict(int, a=1, b=2), defaultdict(list, c=[3, 4]))

# Tuple with ChainMap
chainmap_tuple = (ChainMap({'a': 1}, {'b': 2}), ChainMap({'c': 3}, {'d': 4}))

# Tuple with UserDict
userdict_tuple = (UserDict(a=1, b=2), UserDict(c=3, d=4))

# Tuple with UserList
userlist_tuple = (UserList([1, 2, 3]), UserList([4, 5, 6]))

# Tuple with UserString
userstring_tuple = (UserString("hello"), UserString("world"))