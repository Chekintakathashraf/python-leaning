# Example 1: Uninitialized local variable
def example1():
    # print(x)  # Error: local variable 'x' referenced before assignment
    x = 10
    print(x)
example1()

# Example 2: Local variable shadowing global variable
x = 5
def example2():
    x = 10
    print(x)  # Correct: prints 10
example2()

# Example 3: Using local variable before assignment
def example3():
    # print(x)  # Error: local variable 'x' referenced before assignment
    x = 10
    print(x)
example3()

# Example 4: Modifying global variable without global keyword
y = 5
def example4():
    # y += 1  # Error: UnboundLocalError: local variable 'y' referenced before assignment
    global y
    y += 1
    print(y)
example4()

# Example 5: Using nonlocal variable without nonlocal keyword
def outer():
    z = 5
    def inner():
        # z += 1  # Error: UnboundLocalError: local variable 'z' referenced before assignment
        nonlocal z
        z += 1
        print(z)
    inner()
outer()

# Example 6: Using local variable in a nested function
def example6():
    a = 10
    def nested():
        print(a)  # Correct: prints 10
    nested()
example6()

# Example 7: Local variable in a loop
def example7():
    for i in range(5):
        pass
    # print(i)  # Error: 'i' is not defined outside the loop
example7()

# Example 8: Local variable in a conditional block
def example8():
    if True:
        b = 10
    print(b)  # Correct: prints 10
example8()

# Example 9: Local variable in a try-except block
def example9():
    try:
        c = 10
    except:
        pass
    print(c)  # Correct: prints 10
example9()

# Example 10: Local variable in a function with default argument
def example10(d=10):
    print(d)  # Correct: prints 10
example10()

# Example 11: Local variable in a list comprehension
def example11():
    e = [i for i in range(5)]
    print(e)  # Correct: prints [0, 1, 2, 3, 4]
example11()

# Example 12: Local variable in a generator expression
def example12():
    f = (i for i in range(5))
    print(list(f))  # Correct: prints [0, 1, 2, 3, 4]
example12()

# Example 13: Local variable in a lambda function
def example13():
    g = lambda x: x + 10
    print(g(5))  # Correct: prints 15
example13()

# Example 14: Local variable in a class method
class Example14:
    def method(self):
        h = 10
        print(h)  # Correct: prints 10
Example14().method()

# Example 15: Local variable in a static method
class Example15:
    @staticmethod
    def method():
        i = 10
        print(i)  # Correct: prints 10
Example15.method()

# Example 16: Local variable in a class variable
class Example16:
    j = 10
    def method(self):
        print(self.j)  # Correct: prints 10
Example16().method()

# Example 17: Local variable in a class instance variable
class Example17:
    def __init__(self):
        self.k = 10
    def method(self):
        print(self.k)  # Correct: prints 10
Example17().method()

# Example 18: Local variable in a class property
class Example18:
    @property
    def l(self):
        return 10
    def method(self):
        print(self.l)  # Correct: prints 10
Example18().method()

# Example 19: Local variable in a class method with decorator
class Example19:
    @classmethod
    def method(cls):
        m = 10
        print(m)  # Correct: prints 10
Example19.method()

# Example 20: Local variable in a function with variable arguments
def example20(*args):
    n = sum(args)
    print(n)  # Correct: prints the sum of args
example20(1, 2, 3)