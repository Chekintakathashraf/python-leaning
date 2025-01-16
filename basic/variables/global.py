# Example 1: Basic global variable
x = 10

def print_global():
    print(x)

print_global()

# Example 2: Modifying global variable inside a function
y = 20

def modify_global():
    global y
    y = 30

modify_global()
print(y)

# Example 3: Using global variable in multiple functions
z = 40

def func1():
    global z
    z += 10

def func2():
    global z
    z *= 2

func1()
func2()
print(z)

# Example 4: Global variable with same name as local variable
a = 50

def local_global_conflict():
    a = 60
    print("Local a:", a)
    print("Global a:", globals()['a'])

local_global_conflict()

# Example 5: Accessing global variable inside a class
b = 70

class MyClass:
    def print_global_b(self):
        print(b)

obj = MyClass()
obj.print_global_b()

# Example 6: Modifying global variable inside a class
c = 80

class MyClass2:
    def modify_global_c(self):
        global c
        c = 90

obj2 = MyClass2()
obj2.modify_global_c()
print(c)

# Example 7: Using global variable in nested functions
d = 100

def outer_function():
    def inner_function():
        print(d)
    inner_function()

outer_function()

# Example 8: Modifying global variable in nested functions
e = 110

def outer_function2():
    global e
    e = 120
    def inner_function2():
        global e
        e = 130
    inner_function2()

outer_function2()
print(e)

# Example 9: Using global variable in a loop
f = 140

for i in range(3):
    print(f)

# Example 10: Modifying global variable in a loop
g = 150

def modify_global_in_loop():
    global g
    for i in range(3):
        g += 10

modify_global_in_loop()
print(g)

# Example 11: Using global variable in a list comprehension
h = 160

list_comp = [h for _ in range(3)]
print(list_comp)

# Example 12: Modifying global variable in a list comprehension
i = 170

list_comp2 = [i + 10 for _ in range(3)]
print(list_comp2)

# Example 13: Using global variable in a dictionary comprehension
j = 180

dict_comp = {k: j for k in range(3)}
print(dict_comp)

# Example 14: Modifying global variable in a dictionary comprehension
k = 190

dict_comp2 = {k: k + 10 for k in range(3)}
print(dict_comp2)

# Example 15: Using global variable in a lambda function
l = 200

lambda_func = lambda x: x + l
print(lambda_func(10))

# Example 16: Modifying global variable in a lambda function
m = 210

lambda_func2 = lambda x: x + m
m = 220
print(lambda_func2(10))

# Example 17: Using global variable in a generator function
n = 230

def generator_func():
    yield n

gen = generator_func()
print(next(gen))

# Example 18: Modifying global variable in a generator function
o = 240

def generator_func2():
    global o
    o = 250
    yield o

gen2 = generator_func2()
print(next(gen2))

# Example 19: Using global variable in a decorator
p = 260

def my_decorator(func):
    def wrapper():
        print(p)
        func()
    return wrapper

@my_decorator
def my_function():
    print("Hello")

my_function()

# Example 20: Modifying global variable in a decorator
q = 270

def my_decorator2(func):
    def wrapper():
        global q
        q = 280
        func()
    return wrapper

@my_decorator2
def my_function2():
    print("Hello")

my_function2()
print(q)