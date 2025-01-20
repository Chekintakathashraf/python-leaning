# Example 1: Simple local variable
def example1():
    local_var = 10
    print(local_var)

# Example 2: Simple global variable
global_var = 20
def example2():
    print(global_var)

# Example 3: Modifying global variable inside function
def example3():
    global global_var
    global_var = 30
    print(global_var)

# Example 4: Local variable with the same name as global variable
global_var = 40
def example4():
    global_var = 50
    print(global_var)

# Example 5: Accessing global variable inside function
global_var = 60
def example5():
    print(global_var)

# Example 6: Using global variable in a loop
global_var = 70
def example6():
    for i in range(3):
        print(global_var)

# Example 7: Using local variable in a loop
def example7():
    for i in range(3):
        local_var = i
        print(local_var)

# Example 8: Nested functions with local variables
def example8():
    def inner_function():
        local_var = 80
        print(local_var)
    inner_function()

# Example 9: Nested functions with global variables
global_var = 90
def example9():
    def inner_function():
        print(global_var)
    inner_function()

# Example 10: Modifying global variable in nested function
global_var = 100
def example10():
    def inner_function():
        global global_var
        global_var = 110
    inner_function()
    print(global_var)

# Example 11: Local variable in conditional statement
def example11():
    if True:
        local_var = 120
    print(local_var)

# Example 12: Global variable in conditional statement
global_var = 130
def example12():
    if True:
        print(global_var)

# Example 13: Local variable in try-except block
def example13():
    try:
        local_var = 140
    except:
        pass
    print(local_var)

# Example 14: Global variable in try-except block
global_var = 150
def example14():
    try:
        print(global_var)
    except:
        pass

# Example 15: Local variable in function argument
def example15(local_var):
    print(local_var)

# Example 16: Global variable in function argument
global_var = 160
def example16(arg):
    print(global_var, arg)

# Example 17: Local variable in list comprehension
def example17():
    local_var = [i for i in range(3)]
    print(local_var)

# Example 18: Global variable in list comprehension
global_var = 170
def example18():
    local_var = [global_var for i in range(3)]
    print(local_var)

# Example 19: Local variable in dictionary comprehension
def example19():
    local_var = {i: i*2 for i in range(3)}
    print(local_var)

# Example 20: Global variable in dictionary comprehension
global_var = 180
def example20():
    local_var = {i: global_var for i in range(3)}
    print(local_var)

# Example 21: Local variable in set comprehension
def example21():
    local_var = {i for i in range(3)}
    print(local_var)

# Example 22: Global variable in set comprehension
global_var = 190
def example22():
    local_var = {global_var for i in range(3)}
    print(local_var)

# Example 23: Local variable in generator expression
def example23():
    local_var = (i for i in range(3))
    print(list(local_var))

# Example 24: Global variable in generator expression
global_var = 200
def example24():
    local_var = (global_var for i in range(3))
    print(list(local_var))

# Example 25: Local variable in lambda function
def example25():
    local_var = lambda x: x + 1
    print(local_var(1))

# Example 26: Global variable in lambda function
global_var = 210
def example26():
    local_var = lambda x: x + global_var
    print(local_var(1))

# Example 27: Local variable in class method
class Example27:
    def method(self):
        local_var = 220
        print(local_var)

# Example 28: Global variable in class method
global_var = 230
class Example28:
    def method(self):
        print(global_var)

# Example 29: Local variable in class attribute
class Example29:
    local_var = 240
    def method(self):
        print(self.local_var)

# Example 30: Global variable in class attribute
global_var = 250
class Example30:
    global_var = global_var
    def method(self):
        print(self.global_var)