

# SyntaxError
try:
    eval('x === x')
except SyntaxError as e:
    print(f"SyntaxError: {e}")

# NameError
try:
    print(undefined_variable)
except NameError as e:
    print(f"NameError: {e}")

# TypeError
try:
    result = '2' + 2
except TypeError as e:
    print(f"TypeError: {e}")

# IndexError
try:
    lst = [1, 2, 3]
    print(lst[5])
except IndexError as e:
    print(f"IndexError: {e}")

# KeyError
try:
    d = {'a': 1}
    print(d['b'])
except KeyError as e:
    print(f"KeyError: {e}")

# AttributeError
try:
    NoneType = type(None)
    NoneType.some_method()
except AttributeError as e:
    print(f"AttributeError: {e}")

# ValueError
try:
    int('abc')
except ValueError as e:
    print(f"ValueError: {e}")

# ZeroDivisionError
try:
    result = 1 / 0
except ZeroDivisionError as e:
    print(f"ZeroDivisionError: {e}")

# ImportError
try:
    import non_existent_module
except ImportError as e:
    print(f"ImportError: {e}")

# FileNotFoundError
try:
    with open('non_existent_file.txt', 'r') as file:
        content = file.read()
except FileNotFoundError as e:
    print(f"FileNotFoundError: {e}")