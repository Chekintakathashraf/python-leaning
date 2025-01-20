# Simple function with no parameters and no return value
def greet():
    print("Hello, World!")

# Function with parameters
def add(a, b):
    return a + b

# Function with default parameters
def greet_person(name="Guest"):
    print(f"Hello, {name}!")

# Function with variable number of arguments
def sum_all(*args):
    return sum(args)

# Function with keyword arguments
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Recursive function
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Lambda function
square = lambda x: x * x

# Function with a docstring
def multiply(a, b):
    """
    This function multiplies two numbers.
    :param a: First number
    :param b: Second number
    :return: Product of a and b
    """
    return a * b

# Main block to test the functions
if __name__ == "__main__":
    greet()
    print(add(2, 3))
    greet_person("Ashraf")
    greet_person()
    print(sum_all(1, 2, 3, 4, 5))
    print_info(name="Ashraf", age=30, country="Egypt")
    print(factorial(5))
    print(square(4))
    print(multiply(3, 4))