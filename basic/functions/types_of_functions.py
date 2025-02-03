"""
Python Function Types Example
This script demonstrates different types of functions in Python
"""

from functools import partial

# 1. Built-in Functions
print(len("Hello"))  # len() is a built-in function
print(sum([1, 2, 3, 4, 5]))  # sum() returns the total

# 2. User-Defined Functions
def greet(name):
    """Simple user-defined function"""
    return f"Hello, {name}!"

print(greet("Alice"))

# 3. Lambda (Anonymous) Functions
square = lambda x: x * x
print(square(5))  # Output: 25

# 4. Recursive Function
def factorial(n):
    """Returns factorial of a number using recursion"""
    if n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))  # Output: 120

# 5. Higher-Order Functions
def apply_twice(func, x):
    """Applies a function twice"""
    return func(func(x))

def double(n):
    return n * 2

print(apply_twice(double, 5))  # Output: 20

# 6. Generator Function
def countdown(n):
    """Yields numbers from n to 1"""
    while n > 0:
        yield n
        n -= 1

for num in countdown(5):
    print(num)

# 7. Coroutine Function
def simple_coroutine():
    """Coroutine example using yield"""
    while True:
        x = yield
        print(f"Received: {x}")

coroutine = simple_coroutine()
next(coroutine)  # Prime the coroutine
coroutine.send(10)  # Output: Received: 10

# 8. Nested Functions
def outer_function(msg):
    """Function inside another function"""
    def inner_function():
        print(f"Message: {msg}")
    inner_function()

outer_function("Hello, world!")

# 9. First-Class Functions
def greet(name):
    return f"Hello, {name}!"

func = greet  # Assigning function to a variable
print(func("Alice"))  # Output: Hello, Alice!

# 10. Partial Functions
def power(base, exponent):
    """Computes base to the power of exponent"""
    return base ** exponent

square = partial(power, exponent=2)
print(square(4))  # Output: 16
