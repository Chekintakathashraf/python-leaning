"""
    Python LEGB Rule (Scope Resolution)

In Python, the LEGB rule defines the order in which variable names are looked up in different scopes:

    L – Local scope: Variables defined inside the current function.
    E – Enclosing scope: Variables from outer functions (only in nested functions).
    G – Global scope: Variables defined at the top level of a script/module.
    B – Built-in scope: Predefined names in Python (e.g., len, print, etc.).
    
    """
    
#Example 1: Demonstrating LEGB Rule

# Global variable
x = "global x"

def outer_function():
    # Enclosing variable
    x = "enclosing x"

    def inner_function():
        # Local variable
        x = "local x"
        print("Inside inner_function:", x)  # Local scope

    inner_function()
    print("Inside outer_function:", x)  # Enclosing scope

outer_function()
print("In global scope:", x)  # Global scope

#output 
""" 
Inside inner_function: local x
Inside outer_function: enclosing x
In global scope: global x
"""

#Example 2: Using global and nonlocal Keywords

"""
When modifying variables across scopes, use:

    global: To modify a global variable inside a function.
    nonlocal: To modify an enclosing variable inside nested functions
    
    """

x = 10  # Global variable

def modify_global():
    global x
    x = 20  # Modifies the global x
    print("Inside function:", x)

modify_global()
print("Outside function:", x)

#output
"""
Inside function: 20
Outside function: 20

"""

#Using nonlocal keyword

def outer_function():
    x = 10  # Enclosing variable

    def inner_function():
        nonlocal x
        x = 20  # Modifies the enclosing x
        print("Inside inner_function:", x)

    inner_function()
    print("Inside outer_function:", x)

outer_function()

"""
Inside inner_function: 20
Inside outer_function: 20
"""

#Example 3: LEGB with Multiple Nested Functions

x = "global x"  # Global variable

def outer():
    x = "enclosing outer x"  # Enclosing variable

    def inner1():
        x = "enclosing inner1 x"  # Enclosing for inner2

        def inner2():
            x = "enclosing inner2 x"  # Enclosing for inner3

            def inner3():
                x = "local x"  # Local to inner3
                print("Inside inner3:", x)  # Local scope

            inner3()
            print("Inside inner2:", x)  # Enclosing inner2 scope

        inner2()
        print("Inside inner1:", x)  # Enclosing inner1 scope

    inner1()
    print("Inside outer:", x)  # Enclosing outer scope

outer()
print("In global scope:", x)  # Global scope

#output

"""
Inside inner3: local x
Inside inner2: enclosing inner2 x
Inside inner1: enclosing inner1 x
Inside outer: enclosing outer x
In global scope: global x

explanation

The inner3() function prints "local x" because it's defined in its local scope.
inner2() prints "enclosing inner2 x" from its enclosing scope.
inner1() prints "enclosing inner1 x", showing access to its enclosing scope.
outer() prints "enclosing outer x", the variable in the enclosing outer function.
Finally, the global variable "global x" is printed outside all functions.
"""

#Example 4: Demonstrating global and nonlocal in Nested Functions

x = "global x"

def outer():
    x = "enclosing x"

    def inner1():
        nonlocal x
        x = "modified enclosing x"
        
        def inner2():
            global x
            x = "modified global x"
            print("Inside inner2:", x)
        
        inner2()
        print("Inside inner1:", x)

    inner1()
    print("Inside outer:", x)

outer()
print("In global scope:", x)

#output
"""
Inside inner2: modified global x
Inside inner1: modified enclosing x
Inside outer: modified enclosing x
In global scope: modified global x

Explanation:

    inner2() modifies the global x using global x.
    inner1() modifies the enclosing x using nonlocal x.
    The changes reflect accordingly when accessed in different scopes.
    
    """
    
#Example 5: LEGB with Built-in Scope
    
def my_function():
    len = 5  # Overrides built-in len function
    print("Length:", len)

my_function()

# Using built-in len function outside the function scope
print("Actual length:", len([1, 2, 3, 4]))

"""
Length: 5
Actual length: 4

Explanation:

    Inside my_function, the built-in len is overridden by a local variable.
    Outside the function, the actual len() function works correctly.
    """
    
#Example 6: Mixing Local, Nonlocal, and Global Scopes

x = "global"

def outer():
    x = "outer"

    def inner():
        nonlocal x
        x = "inner"

        def innermost():
            global x
            x = "global modified"
        
        innermost()
        print("Inside inner:", x)

    inner()
    print("Inside outer:", x)

outer()
print("In global scope:", x)

#output
"""
Inside inner: inner
Inside outer: inner
In global scope: global modified

Explanation:

    nonlocal in inner() modifies outer's x.
    global in innermost() modifies the global x.
    """
    
    

