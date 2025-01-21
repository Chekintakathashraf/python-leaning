# Example of basic exception handling with try and except
try:
    result = 10 / 0
except ZeroDivisionError:
    print("You can't divide by zero!")

# Example of exception handling with multiple except blocks
try:
    result = int("abc")
except ValueError:
    print("ValueError: Invalid literal for int()")
except TypeError:
    print("TypeError: An error occurred")

# Example of exception handling with else block
try:
    result = 10 / 2
except ZeroDivisionError:
    print("You can't divide by zero!")
else:
    print("Division successful, result is:", result)

# Example of exception handling with finally block
try:
    result = 10 / 0
except ZeroDivisionError:
    print("You can't divide by zero!")
finally:
    print("This will always execute, regardless of an exception")

# Example of exception handling with if, elif, else
try:
    value = int(input("Enter a number: "))
    if value < 0:
        raise ValueError("Negative value entered")
    elif value == 0:
        raise ValueError("Zero entered")
    else:
        print("Positive value entered:", value)
except ValueError as e:
    print("ValueError:", e)
finally:
    print("Input handling complete")