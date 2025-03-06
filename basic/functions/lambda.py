"""
Python Lambda Function Examples
--------------------------------
This script contains all possible use cases of lambda functions.
Each example is properly commented to explain its functionality.
"""

from functools import reduce

# 1️⃣ Basic Lambda Functions
square = lambda x: x ** 2  # Single argument
multiply = lambda x, y: x * y  # Multiple arguments
hello = lambda: "Hello, World!"  # No arguments
max_num = lambda x, y: x if x > y else y  # Using if-else

print(square(4))  # Output: 16
print(multiply(3, 4))  # Output: 12
print(hello())  # Output: Hello, World!
print(max_num(5, 9))  # Output: 9

# 2️⃣ Using lambda with map(), filter(), reduce()
nums = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, nums))  # Square each number
evens = list(filter(lambda x: x % 2 == 0, nums))  # Filter even numbers
product = reduce(lambda x, y: x * y, nums)  # Multiply all elements

print(squared)  # Output: [1, 4, 9, 16, 25]
print(evens)  # Output: [2, 4]
print(product)  # Output: 120

# 3️⃣ Using lambda with sorting
pairs = [(1, 2), (3, 1), (5, 0), (2, 4)]
pairs.sort(key=lambda x: x[1])  # Sort by second element
print(pairs)  # Output: [(5, 0), (3, 1), (1, 2), (2, 4)]

students = [{'name': 'Alice', 'age': 25}, {'name': 'Bob', 'age': 20}]
students.sort(key=lambda x: x['age'])
print(students)  # Output: Sorted by age

# 4️⃣ Using lambda in list comprehension
doubled = [(lambda x: x * 2)(x) for x in nums]
print(doubled)  # Output: [2, 4, 6, 8, 10]

# 5️⃣ Using lambda with any() and all()
print(any(map(lambda x: x % 2 == 0, nums)))  # True if any even number exists
print(all(map(lambda x: x > 0, nums)))  # True if all numbers are positive

# 6️⃣ Using lambda with zip()
list1, list2 = [1, 2, 3], [4, 5, 6]
sum_list = list(map(lambda x, y: x + y, list1, list2))
print(sum_list)  # Output: [5, 7, 9]

# 7️⃣ Using lambda with enumerate()
words = ["apple", "banana", "cherry"]
indexed_words = list(map(lambda x: (x[0], x[1]), enumerate(words)))
print(indexed_words)  # Output: [(0, 'apple'), (1, 'banana'), (2, 'cherry')]

# 8️⃣ Using lambda with default arguments
greet = lambda name="Guest": f"Hello, {name}!"
print(greet())  # Output: Hello, Guest!
print(greet("Alice"))  # Output: Hello, Alice!

# 9️⃣ Using lambda inside a dictionary
operations = {
    "add": lambda x, y: x + y,
    "sub": lambda x, y: x - y,
    "mul": lambda x, y: x * y
}
print(operations["add"](5, 3))  # Output: 8

# 🔟 Nested lambda functions
nested_lambda = lambda x: (lambda y: x + y)
add_five = nested_lambda(5)
print(add_five(3))  # Output: 8

# 1️⃣1️⃣ Recursive lambda function (Factorial)
factorial = lambda n: 1 if n == 0 else n * factorial(n - 1)
print(factorial(5))  # Output: 120

# 1️⃣2️⃣ Lambda with boolean operations
is_even = lambda x: x % 2 == 0
is_adult = lambda age: age >= 18 and "Adult" or "Minor"
print(is_even(4))  # Output: True
print(is_adult(20))  # Output: Adult
