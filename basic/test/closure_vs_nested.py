def outer_function(msg):
    def inner_function():  
        print(f"Message: {msg}")  

    inner_function()  

outer_function("Hello, Nested Function!")  

def outer_closure_function(msg):
    def inner_closure_function():  
        print(f"Message: {msg}")  

    return inner_closure_function

call = outer_closure_function("Hello, closure Function!") 
call() 