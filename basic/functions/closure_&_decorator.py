def repeat(n):  # Outer function (closure)
    def decorator(func):  # Decorator function
        def wrapper():
            for _ in range(n):  # `n` is remembered (closure property)
                func()
        return wrapper
    return decorator

@repeat(3)
def say_hi():
    print("Hi!")

say_hi()
