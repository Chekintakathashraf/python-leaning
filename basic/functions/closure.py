# Nested function example
def nested_example(x):
    def inner_function(y):
        return x + y
    return inner_function(10)

print(nested_example(5))  # Output: 15

# Closure example
def closure_example(x):
    def inner_function(y):
        return x + y
    return inner_function

add_five = closure_example(5)
print(add_five(10))  # Output: 15


# Example 1
def outer_function(x):
    def inner_function(y):
        return x + y
    return inner_function

add_five = outer_function(5)
print(add_five(10))  # Output: 15



# Example 2
def make_multiplier_of(n):
    def multiplier(x):
        return x * n
    return multiplier

times3 = make_multiplier_of(3)
print(times3(9))  # Output: 27

# Example 3
def power_of(exponent):
    def power(base):
        return base ** exponent
    return power

square = power_of(2)
print(square(4))  # Output: 16

# Example 4
def greeting(name):
    def say_hello():
        return f"Hello, {name}!"
    return say_hello

hello_john = greeting("John")
print(hello_john())  # Output: Hello, John!

# Example 5
def make_adder(x):
    def adder(y):
        return x + y
    return adder

add_ten = make_adder(10)
print(add_ten(5))  # Output: 15

# Example 6
def counter():
    count = 0
    def increment():
        nonlocal count
        count += 1
        return count
    return increment

count_up = counter()
print(count_up())  # Output: 1
print(count_up())  # Output: 2

# Example 7
def make_divider_of(n):
    def divider(x):
        return x / n
    return divider

divide_by_2 = make_divider_of(2)
print(divide_by_2(10))  # Output: 5.0

# Example 8
def make_repeater_of(n):
    def repeater(string):
        return string * n
    return repeater

repeat_3 = make_repeater_of(3)
print(repeat_3("Hello "))  # Output: Hello Hello Hello 

# Example 9
def make_subtractor_of(n):
    def subtractor(x):
        return x - n
    return subtractor

subtract_5 = make_subtractor_of(5)
print(subtract_5(20))  # Output: 15

# Example 10
def make_greeter(greeting):
    def greeter(name):
        return f"{greeting}, {name}!"
    return greeter

say_hi = make_greeter("Hi")
print(say_hi("Alice"))  # Output: Hi, Alice!



