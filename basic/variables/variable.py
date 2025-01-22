#LEGB Rule in Python (functional-Based Explanation)

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
    
    

#LEGB Rule in Python (Class-Based Explanation)

"""

When dealing with classes in Python, the LEGB rule still applies, but with a few nuances due to the object-oriented structure. In a class-based context, scope resolution works slightly differently because:

    Instance (Object) Scope: Variables stored in self (instance attributes).
    Class Scope: Variables shared across instances, stored in the class definition.
    Global Scope: Variables defined outside the class.
    Built-in Scope: Standard Python built-in functions and names.
    
    """
    
#Example 1: Basic Class-Based LEGB Example

x = "global x"  # Global scope

class MyClass:
    x = "class x"  # Class scope (Enclosing)

    def my_method(self):
        x = "local x"  # Local scope
        print("Inside method:", x)

obj = MyClass()
obj.my_method()
print("In class scope:", obj.x)
print("In global scope:", x)

#output
"""
Inside method: local x
In class scope: class x
In global scope: global x

Explanation:

    Inside my_method, x refers to the local scope.
    The x inside the class refers to the class-level scope.
    Outside the class, the global x is accessed.
    """
    
#Example 2: Using self for Instance Attributes (Local vs Instance Scope)

x = "global x"

class Example:
    x = "class x"

    def __init__(self, x):
        self.x = x  # Instance variable (specific to an object)

    def show_x(self):
        x = "local x"
        print("Local scope:", x)
        print("Instance scope:", self.x)
        print("Class scope:", Example.x)
        print("Global scope:", globals()['x'])

obj = Example("instance x")
obj.show_x()

#output
"""
Local scope: local x
Instance scope: instance x
Class scope: class x
Global scope: global x

Explanation:

    self.x accesses the instance attribute.
    Example.x accesses the class attribute.
    globals()['x'] retrieves the global x.
    The local variable inside the method shadows all others.
    """

#Example 3: Accessing Enclosing Scope in Nested Methods

class OuterClass:
    x = "class x"

    def outer_method(self):
        x = "outer x"

        class InnerClass:
            def inner_method(self):
                x = "inner x"
                print("Local scope:", x)
                print("Enclosing scope:", outer_instance.x)
                print("Class scope:", OuterClass.x)
                print("Global scope:", globals()['x'])

        outer_instance = OuterClass()
        inner_obj = InnerClass()
        inner_obj.inner_method()

x = "global x"
obj = OuterClass()
obj.outer_method()

#output
"""
Local scope: inner x
Enclosing scope: outer x
Class scope: class x
Global scope: global x

Explanation:

    The method inner_method() has its own local scope.
    The enclosing function variable from outer_method() is accessed using outer_instance.x.
    Class-level scope is accessed via OuterClass.x.
    The global scope is accessed using globals()['x'].
    """
    
#Example 4: Using global and nonlocal in Class Methods

x = "global x"

class Test:
    x = "class x"

    def outer_method(self):
        nonlocal_x = "outer x"

        def inner_method():
            nonlocal nonlocal_x  # Modify the outer_method's variable
            nonlocal_x = "modified outer x"

            global x  # Modify the global variable
            x = "modified global x"

        inner_method()
        print("After inner_method in outer_method:", nonlocal_x)

obj = Test()
obj.outer_method()
print("Global scope after modification:", x)

# if u want to use same x for local,global,

# a variable cannot be both global and nonlocal within the same function. If you try to declare x as both, Python throws the error: SyntaxError: name 'x' is assigned to before global declaration.

#output
"""
After inner_method in outer_method: modified outer x
Global scope after modification: modified global x

Explanation:

    nonlocal x modifies outer x inside outer_method.
    global x modifies the global x outside the class.
    """
    
#Example 5: Multiple Nested Classes with LEGB

x = "global x"

class Outer:
    x = "outer class x"

    class Inner:
        x = "inner class x"

        def inner_method(self):
            x = "local x"
            print("Local:", x)
            print("Enclosing (Outer class):", Outer.x)
            print("Class (Inner class):", self.x)
            print("Global:", globals()['x'])

obj = Outer.Inner()
obj.inner_method()

#output
"""
Local: local x
Enclosing (Outer class): outer class x
Class (Inner class): inner class x
Global: global x

Explanation:

    The local variable x inside the method shadows all others.
    Outer.x refers to the outer class variable.
    self.x accesses the inner class variable.
    The global variable x is retrieved using globals()['x'].
    """

#Example 6: Overriding Built-in Scope in Classes

class OverrideExample:
    len = 100  # Overrides built-in len

    def check_len(self):
        len = 50  # Local scope
        print("Local len:", len)
        print("Class len:", self.len)
        print("Built-in len:", __builtins__.len([1, 2, 3]))

obj = OverrideExample()
obj.check_len()

#output
"""
Local len: 50
Class len: 100
Built-in len: 3

Explanation:

    The method variable len shadows the class variable.
    The class variable len shadows the built-in len.
    The built-in len() is accessed using __builtins__.len().
    """
    