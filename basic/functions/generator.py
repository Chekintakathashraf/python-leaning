# Normal function to generate Fibonacci sequence
def fibonacci_normal(n):
    fib_sequence = []
    a, b = 0, 1
    while len(fib_sequence) < n:
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence

print(fibonacci_normal(10))  # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

# Generator function to generate Fibonacci sequence
def fibonacci_generator(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

print(list(fibonacci_generator(10)))  # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

# Custom generator function
def custom_generator(start, end):
    current = start
    while current < end:
        yield current
        current += 1

print(list(custom_generator(5, 10)))  # [5, 6, 7, 8, 9]

# Generator expression
gen_expr = (x * x for x in range(10))

print(list(gen_expr))  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# List comprehension vs Generator expression
list_comp = [x * x for x in range(10)]
gen_expr = (x * x for x in range(10))

print(list_comp)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(list(gen_expr))  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Example 1: Normal function to generate squares
def squares_normal(n):
    return [x * x for x in range(n)]

print(squares_normal(10))  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Example 2: Generator function to generate squares
def squares_generator(n):
    for x in range(n):
        yield x * x

print(list(squares_generator(10)))  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Example 3: Custom generator to generate even numbers
def even_numbers_generator(n):
    for x in range(n):
        if x % 2 == 0:
            yield x

print(list(even_numbers_generator(10)))  # [0, 2, 4, 6, 8]

# Example 4: Generator expression for even numbers
even_gen_expr = (x for x in range(10) if x % 2 == 0)

print(list(even_gen_expr))  # [0, 2, 4, 6, 8]

# Example 5: Normal function to generate prime numbers
def primes_normal(n):
    primes = []
    for num in range(2, n + 1):
        if all(num % i != 0 for i in range(2, int(num ** 0.5) + 1)):
            primes.append(num)
    return primes

print(primes_normal(20))  # [2, 3, 5, 7, 11, 13, 17, 19]

# Example 6: Generator function to generate prime numbers
def primes_generator(n):
    for num in range(2, n + 1):
        if all(num % i != 0 for i in range(2, int(num ** 0.5) + 1)):
            yield num

print(list(primes_generator(20)))  # [2, 3, 5, 7, 11, 13, 17, 19]

# Example 7: Generator function to generate infinite sequence
def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1

# gen = infinite_sequence()
# for _ in range(10):
#     print(next(gen))  # 0, 1, 2, 3, 4, 5, 6, 7, 8, 9

# Example 8: Generator function to read file line by line
def read_file_line_by_line(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            yield line

# for line in read_file_line_by_line('example.txt'):
#     print(line)

# Example 9: Generator function to generate factorials
def factorial_generator(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
        yield fact

print(list(factorial_generator(5)))  # [1, 2, 6, 24, 120]

# Example 10: Generator function to generate Fibonacci sequence up to a limit
def fibonacci_up_to_limit(limit):
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b

print(list(fibonacci_up_to_limit(50)))  # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

# Example 11: Generator function to generate geometric progression
def geometric_progression(a, r, n):
    for i in range(n):
        yield a * (r ** i)

print(list(geometric_progression(2, 3, 5)))  # [2, 6, 18, 54, 162]

# Example 12: Generator function to generate arithmetic progression
def arithmetic_progression(a, d, n):
    for i in range(n):
        yield a + i * d

print(list(arithmetic_progression(2, 3, 5)))  # [2, 5, 8, 11, 14]

# Example 13: Generator function to generate triangular numbers
def triangular_numbers(n):
    for i in range(1, n + 1):
        yield i * (i + 1) // 2

print(list(triangular_numbers(5)))  # [1, 3, 6, 10, 15]

# Example 14: Generator function to generate square numbers
def square_numbers(n):
    for i in range(1, n + 1):
        yield i * i

print(list(square_numbers(5)))  # [1, 4, 9, 16, 25]

# Example 15: Generator function to generate cube numbers
def cube_numbers(n):
    for i in range(1, n + 1):
        yield i * i * i

print(list(cube_numbers(5)))  # [1, 8, 27, 64, 125]

# Example 16: Generator function to generate powers of 2
def powers_of_2(n):
    for i in range(n):
        yield 2 ** i

print(list(powers_of_2(5)))  # [1, 2, 4, 8, 16]

# Example 17: Generator function to generate Fibonacci sequence using memoization
def fibonacci_memoization(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci_memoization(n - 1, memo) + fibonacci_memoization(n - 2, memo)
    return memo[n]

print(fibonacci_memoization(10))  # 55

# Example 18: Generator function to generate Lucas numbers
def lucas_numbers(n):
    a, b = 2, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

print(list(lucas_numbers(10)))  # [2, 1, 3, 4, 7, 11, 18, 29, 47, 76]

# Example 19: Generator function to generate Pell numbers
def pell_numbers(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, 2 * b + a

print(list(pell_numbers(10)))  # [0, 1, 2, 5, 12, 29, 70, 169, 408, 985]

# Example 20: Generator function to generate Catalan numbers
def catalan_numbers(n):
    def binomial_coeff(n, k):
        if k > n - k:
            k = n - k
        res = 1
        for i in range(k):
            res *= (n - i)
            res //= (i + 1)
        return res

    for i in range(n):
        yield binomial_coeff(2 * i, i) // (i + 1)

print(list(catalan_numbers(10)))  # [1, 1, 2, 5, 14, 42, 132, 429, 1430, 4862]