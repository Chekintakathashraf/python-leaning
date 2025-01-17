# Integer to other types
int_value = 10
float_value = float(int_value)  # int to float
str_value = str(int_value)      # int to str
bool_value = bool(int_value)    # int to bool

# Error examples for Integer to other types
try:
    int_value = "abc"
    float_value = float(int_value)  # ValueError: could not convert string to float: 'abc'
except ValueError as e:
    print(e)

try:
    int_value = "abc"
    int_value = int(int_value)  # ValueError: invalid literal for int() with base 10: 'abc'
except ValueError as e:
    print(e)

# Float to other types
float_value = 10.5
int_value = int(float_value)    # float to int
str_value = str(float_value)    # float to str
bool_value = bool(float_value)  # float to bool

# Error examples for Float to other types
try:
    float_value = "abc"
    float_value = float(float_value)  # ValueError: could not convert string to float: 'abc'
except ValueError as e:
    print(e)

# String to other types
str_value = "123"
int_value = int(str_value)      # str to int
float_value = float(str_value)  # str to float
bool_value = bool(str_value)    # str to bool

# Error examples for String to other types
try:
    str_value = "abc"
    int_value = int(str_value)  # ValueError: invalid literal for int() with base 10: 'abc'
except ValueError as e:
    print(e)

try:
    str_value = "abc"
    float_value = float(str_value)  # ValueError: could not convert string to float: 'abc'
except ValueError as e:
    print(e)

# Boolean to other types
bool_value = True
int_value = int(bool_value)     # bool to int
float_value = float(bool_value) # bool to float
str_value = str(bool_value)     # bool to str

# List to other types
list_value = [1, 2, 3]
str_value = str(list_value)     # list to str
tuple_value = tuple(list_value) # list to tuple
set_value = set(list_value)     # list to set

# Error examples for List to other types
try:
    list_value = [1, 2, 3]
    int_value = int(list_value)  # TypeError: int() argument must be a string, a bytes-like object or a number, not 'list'
except TypeError as e:
    print(e)

try:
    list_value = [1, 2, 3]
    float_value = float(list_value)  # TypeError: float() argument must be a string or a number, not 'list'
except TypeError as e:
    print(e)

# Tuple to other types
tuple_value = (1, 2, 3)
str_value = str(tuple_value)    # tuple to str
list_value = list(tuple_value)  # tuple to list
set_value = set(tuple_value)    # tuple to set

# Error examples for Tuple to other types
try:
    tuple_value = (1, 2, 3)
    int_value = int(tuple_value)  # TypeError: int() argument must be a string, a bytes-like object or a number, not 'tuple'
except TypeError as e:
    print(e)

try:
    tuple_value = (1, 2, 3)
    float_value = float(tuple_value)  # TypeError: float() argument must be a string or a number, not 'tuple'
except TypeError as e:
    print(e)

# Set to other types
set_value = {1, 2, 3}
str_value = str(set_value)      # set to str
list_value = list(set_value)    # set to list
tuple_value = tuple(set_value)  # set to tuple

# Error examples for Set to other types
try:
    set_value = {1, 2, 3}
    int_value = int(set_value)  # TypeError: int() argument must be a string, a bytes-like object or a number, not 'set'
except TypeError as e:
    print(e)

try:
    set_value = {1, 2, 3}
    float_value = float(set_value)  # TypeError: float() argument must be a string or a number, not 'set'
except TypeError as e:
    print(e)
