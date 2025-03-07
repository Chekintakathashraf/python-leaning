def capital(func):
    def inner():
        print("the func is calling")
        msg = func()
        print("the func is called")
        return msg.upper()
    return inner


def greet():
    return 'Hello!'


print(greet())
greet = capital(greet)
print(greet())