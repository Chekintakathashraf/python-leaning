
# Function Decorators
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()

# Method Decorators
# Define the decorator
def my_decorator(func):
    def wrapper(self, *args, **kwargs):
        print("Before the method is called")
        result = func(self, *args, **kwargs)  # Call the original method with self, args, kwargs
        print("After the method is called")
        return result
    return wrapper

# Class with method using the decorator
class MyClass:
    def __init__(self, value):
        self.value = value

    @my_decorator  # Apply the decorator
    def display_value(self):
        print(f"The value is {self.value}")

# Create an instance and call the method
obj = MyClass(10)
obj.display_value()

# Built-in Decorators

@staticmethod
def static_method():
    print("This is a static method.")

@classmethod
def class_method(cls):
    print("This is a class method.")

# Decorators with Arguments
def repeat(num_times):
    def decorator_repeat(func):
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator_repeat

@repeat(num_times=3)
def greet(name):
    print(f"Hello {name}")

greet("Alice")

# Property Decorators
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = value

circle = Circle(5)
print(circle.radius)
circle.radius = 10
print(circle.radius)

# Function with Arguments
def my_decorator_with_args(arg1, arg2):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(f"Arguments passed to decorator: {arg1}, {arg2}")
            return func(*args, **kwargs)
        return wrapper
    return decorator

@my_decorator_with_args("Hello", "World")
def my_function():
    print("Function is called")

my_function()

# Multiple Decorators
def decorator1(func):
    def wrapper():
        print("Decorator 1")
        func()
    return wrapper

def decorator2(func):
    def wrapper():
        print("Decorator 2")
        func()
    return wrapper

@decorator1
@decorator2
def say_hi():
    print("Hi!")

say_hi()

# Class Decorators with Arguments
def class_decorator(arg1, arg2):
    def decorator(cls):
        cls.arg1 = arg1
        cls.arg2 = arg2
        return cls
    return decorator

@class_decorator("Hello", "World")
class MyClassWithArgs:
    pass

print(MyClassWithArgs.arg1)
print(MyClassWithArgs.arg2)