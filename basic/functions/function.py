# 1. Basic Mathematical Functions
def math_functions_demo():
    # abs() - Returns absolute value
    print(abs(-5))  # Output: 5
    
    # round() - Rounds number to nearest integer
    print(round(3.7))  # Output: 4
    
    # max() - Returns largest item
    print(max(1, 2, 3))  # Output: 3
    
    # min() - Returns smallest item
    print(min([1, 2, 3]))  # Output: 1
    
    # sum() - Adds items in iterable
    print(sum([1, 2, 3]))  # Output: 6
    
    # pow() - Returns x to power y
    print(pow(2, 3))  # Output: 8

# 2. Type Conversion Functions
def type_conversion_demo():
    # int() - Converts to integer
    print(int("123"))  # Output: 123
    
    # float() - Converts to float
    print(float("12.34"))  # Output: 12.34
    
    # str() - Converts to string
    print(str(123))  # Output: "123"
    
    # bool() - Converts to boolean
    print(bool(1))  # Output: True
    
    # list() - Converts to list
    print(list("abc"))  # Output: ['a', 'b', 'c']
    
    # tuple() - Converts to tuple
    print(tuple([1, 2, 3]))  # Output: (1, 2, 3)

# 3. Sequence Functions
def sequence_functions_demo():
    # len() - Returns length of sequence
    print(len("hello"))  # Output: 5
    
    # sorted() - Returns sorted list
    print(sorted([3, 1, 2]))  # Output: [1, 2, 3]
    
    # reversed() - Returns reverse iterator
    print(list(reversed([1, 2, 3])))  # Output: [3, 2, 1]
    
    # enumerate() - Returns index-value pairs
    for i, v in enumerate(['a', 'b']):
        print(i, v)  # Output: 0 a, 1 b

# 4. String Functions
def string_functions_demo():
    # upper() - Converts to uppercase
    print("hello".upper())  # Output: HELLO
    
    # lower() - Converts to lowercase
    print("HELLO".lower())  # Output: hello
    
    # split() - Splits string into list
    print("a,b,c".split(","))  # Output: ['a', 'b', 'c']
    
    # join() - Joins iterable elements
    print("-".join(['a', 'b']))  # Output: a-b

# 5. List Functions
def list_functions_demo():
    lst = [1, 2, 3]
    # append() - Adds element to end
    lst.append(4)
    
    # extend() - Adds elements from iterable
    lst.extend([5, 6])
    
    # insert() - Inserts element at index
    lst.insert(0, 0)
    
    # remove() - Removes first occurrence
    lst.remove(3)
    
    print(lst)  # Output: [0, 1, 2, 4, 5, 6]

# 6. Dictionary Functions
def dict_functions_demo():
    d = {'a': 1, 'b': 2}
    # keys() - Returns dict keys
    print(list(d.keys()))  # Output: ['a', 'b']
    
    # values() - Returns dict values
    print(list(d.values()))  # Output: [1, 2]
    
    # items() - Returns key-value pairs
    print(list(d.items()))  # Output: [('a', 1), ('b', 2)]
    
    # get() - Returns value or default
    print(d.get('c', 3))  # Output: 3

# 7. Set Functions
def set_functions_demo():
    s1 = {1, 2, 3}
    s2 = {3, 4, 5}
    
    # union() - Returns union of sets
    print(s1.union(s2))  # Output: {1, 2, 3, 4, 5}
    
    # intersection() - Returns common elements
    print(s1.intersection(s2))  # Output: {3}
    
    # difference() - Returns difference
    print(s1.difference(s2))  # Output: {1, 2}

# 8. File Functions
def file_functions_demo():
    # open() - Opens file
    with open('test.txt', 'w') as f:
        f.write('Hello')
    
    with open('test.txt', 'r') as f:
        print(f.read())  # Output: Hello

# 9. Lambda Functions
def lambda_functions_demo():
    # Lambda function example
    square = lambda x: x**2
    print(square(5))  # Output: 25
    
    # map() with lambda
    numbers = [1, 2, 3]
    squared = list(map(lambda x: x**2, numbers))
    print(squared)  # Output: [1, 4, 9]

# 10. Generator Functions
def generator_function():
    yield 1
    yield 2
    yield 3

def generator_demo():
    gen = generator_function()
    print(list(gen))  # Output: [1, 2, 3]

# Main execution
if __name__ == "__main__":
    math_functions_demo()
    type_conversion_demo()
    sequence_functions_demo()
    string_functions_demo()
    list_functions_demo()
    dict_functions_demo()
    set_functions_demo()
    # file_functions_demo()  # Commented out to avoid file creation
    lambda_functions_demo()
    generator_demo()