def capital(func):
    def inner():
        msg = func()
        return msg.upper()
    return inner

@capital
def greet():
    return 'Hello!'


print(greet())