import asyncio

# iterator.py

# Basic Iterator Example
my_list = [1, 2, 3, 4]
my_iter = iter(my_list)

print(next(my_iter))  # Output: 1
print(next(my_iter))  # Output: 2
print(next(my_iter))  # Output: 3
print(next(my_iter))  # Output: 4

# Iterator with Tuple
my_tuple = (1, 2, 3, 4)
my_iter = iter(my_tuple)

print(next(my_iter))  # Output: 1
print(next(my_iter))  # Output: 2
print(next(my_iter))  # Output: 3
print(next(my_iter))  # Output: 4

# Iterator with String
my_string = "hello"
my_iter = iter(my_string)

print(next(my_iter))  # Output: h
print(next(my_iter))  # Output: e
print(next(my_iter))  # Output: l
print(next(my_iter))  # Output: l
print(next(my_iter))  # Output: o

# Iterator with Dictionary
my_dict = {'a': 1, 'b': 2, 'c': 3}
my_iter = iter(my_dict)

print(next(my_iter))  # Output: a
print(next(my_iter))  # Output: b
print(next(my_iter))  # Output: c

# Custom Iterator
class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 10:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration

my_numbers = MyNumbers()
my_iter = iter(my_numbers)

for num in my_iter:
    print(num)  # Output: 1 2 3 4 5 6 7 8 9 10

# Asynchronous Iterator

class AsyncIterator:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __aiter__(self):
        self.current = self.start
        return self

    async def __anext__(self):
        if self.current >= self.end:
            raise StopAsyncIteration
        self.current += 1
        await asyncio.sleep(1)
        return self.current

async def main():
    async for number in AsyncIterator(1, 5):
        print(number)  # Output: 2 3 4 5

asyncio.run(main())