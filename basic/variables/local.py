# Example 1: Basic local variable
def example1():
    x = 10
    print(x)

example1()

# Example 2: Local variable in a loop
def example2():
    for i in range(5):
        print(i)

example2()

# Example 3: Local variable in a conditional
def example3():
    x = 10
    if x > 5:
        y = x * 2
        print(y)

example3()

# Example 4: Local variable in a nested function
def example4():
    def inner_function():
        z = 20
        print(z)
    inner_function()

example4()

# Example 5: Local variable in a list comprehension
def example5():
    squares = [x**2 for x in range(10)]
    print(squares)

example5()

# Example 6: Local variable in a dictionary comprehension
def example6():
    square_dict = {x: x**2 for x in range(10)}
    print(square_dict)

example6()

# Example 7: Local variable in a set comprehension
def example7():
    square_set = {x**2 for x in range(10)}
    print(square_set)

example7()

# Example 8: Local variable in a generator expression
def example8():
    square_gen = (x**2 for x in range(10))
    for val in square_gen:
        print(val)

example8()

# Example 9: Local variable in a try-except block
def example9():
    try:
        x = 10 / 0
    except ZeroDivisionError:
        y = "Cannot divide by zero"
        print(y)

example9()

# Example 10: Local variable in a class method
class Example10:
    def method(self):
        x = 10
        print(x)

example10_instance = Example10()
example10_instance.method()



# Example 15: Local variable in a list slicing
def example15():
    lst = [1, 2, 3, 4, 5]
    sliced_lst = lst[1:4]
    print(sliced_lst)

example15()

# Example 16: Local variable in a string slicing
def example16():
    s = "Hello, World!"
    sliced_s = s[7:12]
    print(sliced_s)

example16()

# Example 17: Local variable in a tuple unpacking
def example17():
    t = (1, 2, 3)
    a, b, c = t
    print(a, b, c)

example17()

# Example 18: Local variable in a dictionary unpacking
def example18():
    d = {'a': 1, 'b': 2, 'c': 3}
    for key, value in d.items():
        print(key, value)

example18()

# Example 19: Local variable in a list unpacking
def example19():
    lst = [1, 2, 3, 4, 5]
    a, *b, c = lst
    print(a, b, c)

example19()

# Example 20: Local variable in a function with default arguments
def example20(x=10):
    print(x)

example20()

# Example 21: Local variable in a function with variable-length arguments
def example21(*args):
    for arg in args:
        print(arg)

example21(1, 2, 3)

# Example 22: Local variable in a function with keyword arguments
def example22(**kwargs):
    for key, value in kwargs.items():
        print(key, value)

example22(a=1, b=2, c=3)

# Example 23: Local variable in a function with both args and kwargs
def example23(*args, **kwargs):
    for arg in args:
        print(arg)
    for key, value in kwargs.items():
        print(key, value)

example23(1, 2, 3, a=4, b=5)

# Example 24: Local variable in a recursive function
def example24(n):
    if n == 0:
        return 1
    else:
        return n * example24(n-1)

print(example24(5))

# Example 25: Local variable in a function with a closure
def example25():
    def outer_function():
        x = 10
        def inner_function():
            print(x)
        inner_function()
    outer_function()

example25()

# Example 26: Local variable in a function with a decorator
def example26_decorator(func):
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper

@example26_decorator
def example26():
    print("Inside function")

example26()

# Example 27: Local variable in a function with a context manager
def example27():
    with open('example.txt', 'w') as f:
        f.write('Hello, World!')

example27()

# Example 28: Local variable in a function with a generator
def example28():
    def generator():
        for i in range(5):
            yield i
    for value in generator():
        print(value)

example28()


# Example 30: Local variable in a function with a type hint
def example30(x: int) -> int:
    return x * 2

print(example30(5))