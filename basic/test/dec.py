def capital(func):
    def inner():
        print("the capital is  calling before")
        msg = func()
        print("the capital is called after")
        return msg.upper()
    return inner

def adding(func):
    def inner():
        print("the adding is calling before")
        msg = func()
        print("the adding is called after")
        return msg + "!!!"
    return inner

@adding
@capital
def greet():
    return 'Hello!'


print(greet())  