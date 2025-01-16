# Example 1
x = 10

def increment():
    x += 1

increment()
print(x)

"""
Error: UnboundLocalError: local variable 'x' referenced before assignment
Solution: Use the 'global' keyword to modify the global variable inside the function.
"""

# Corrected Code
x = 10

def increment():
    global x
    x += 1

increment()
print(x)

# Example 2
count = 0

def increment():
    count = count + 1

increment()
print(count)

"""
Error: UnboundLocalError: local variable 'count' referenced before assignment
Solution: Use the 'global' keyword to modify the global variable inside the function.
"""

# Corrected Code
count = 0

def increment():
    global count
    count += 1

increment()
print(count)

# Example 3
total = 100

def add_to_total(amount):
    total += amount

add_to_total(50)
print(total)

"""
Error: UnboundLocalError: local variable 'total' referenced before assignment
Solution: Use the 'global' keyword to modify the global variable inside the function.
"""

# Corrected Code
total = 100

def add_to_total(amount):
    global total
    total += amount

add_to_total(50)
print(total)

# Example 4
name = "Alice"

def change_name(new_name):
    name = new_name

change_name("Bob")
print(name)

"""
Error: The global variable 'name' is not modified inside the function.
Solution: Use the 'global' keyword to modify the global variable inside the function.
"""

# Corrected Code
name = "Alice"

def change_name(new_name):
    global name
    name = new_name

change_name("Bob")
print(name)

# Example 5
balance = 1000

def withdraw(amount):
    balance -= amount

withdraw(100)
print(balance)

"""
Error: UnboundLocalError: local variable 'balance' referenced before assignment
Solution: Use the 'global' keyword to modify the global variable inside the function.
"""

# Corrected Code
balance = 1000

def withdraw(amount):
    global balance
    balance -= amount

withdraw(100)
print(balance)

# Example 6
score = 0

def update_score(points):
    score += points

update_score(10)
print(score)

"""
Error: UnboundLocalError: local variable 'score' referenced before assignment
Solution: Use the 'global' keyword to modify the global variable inside the function.
"""

# Corrected Code
score = 0

def update_score(points):
    global score
    score += points

update_score(10)
print(score)

# Example 7
temperature = 25

def increase_temperature(degrees):
    temperature += degrees

increase_temperature(5)
print(temperature)

"""
Error: UnboundLocalError: local variable 'temperature' referenced before assignment
Solution: Use the 'global' keyword to modify the global variable inside the function.
"""

# Corrected Code
temperature = 25

def increase_temperature(degrees):
    global temperature
    temperature += degrees

increase_temperature(5)
print(temperature)

# Example 8
items = []

def add_item(item):
    items.append(item)

add_item("apple")
print(items)

"""
Error: No error, but it's better to avoid using global variables.
Solution: Pass the list as an argument to the function.
"""

# Corrected Code
def add_item(items, item):
    items.append(item)

items = []
add_item(items, "apple")
print(items)

# Example 9
flag = False

def set_flag():
    flag = True

set_flag()
print(flag)

"""
Error: The global variable 'flag' is not modified inside the function.
Solution: Use the 'global' keyword to modify the global variable inside the function.
"""

# Corrected Code
flag = False

def set_flag():
    global flag
    flag = True

set_flag()
print(flag)

# Example 10
counter = 0

def increment_counter():
    counter += 1

increment_counter()
print(counter)

"""
Error: UnboundLocalError: local variable 'counter' referenced before assignment
Solution: Use the 'global' keyword to modify the global variable inside the function.
"""

# Corrected Code
counter = 0

def increment_counter():
    global counter
    counter += 1

increment_counter()
print(counter)

# Example 11
value = 50

def double_value():
    value *= 2

double_value()
print(value)

"""
Error: UnboundLocalError: local variable 'value' referenced before assignment
Solution: Use the 'global' keyword to modify the global variable inside the function.
"""

# Corrected Code
value = 50

def double_value():
    global value
    value *= 2

double_value()
print(value)

# Example 12
status = "inactive"

def activate():
    status = "active"

activate()
print(status)

"""
Error: The global variable 'status' is not modified inside the function.
Solution: Use the 'global' keyword to modify the global variable inside the function.
"""

# Corrected Code
status = "inactive"

def activate():
    global status
    status = "active"

activate()
print(status)

# Example 13
level = 1

def level_up():
    level += 1

level_up()
print(level)

"""
Error: UnboundLocalError: local variable 'level' referenced before assignment
Solution: Use the 'global' keyword to modify the global variable inside the function.
"""

# Corrected Code
level = 1

def level_up():
    global level
    level += 1

level_up()
print(level)

# Example 14
price = 100

def apply_discount(discount):
    price -= discount

apply_discount(10)
print(price)

"""
Error: UnboundLocalError: local variable 'price' referenced before assignment
Solution: Use the 'global' keyword to modify the global variable inside the function.
"""

# Corrected Code
price = 100

def apply_discount(discount):
    global price
    price -= discount

apply_discount(10)
print(price)

# Example 15
speed = 60

def increase_speed(increment):
    speed += increment

increase_speed(10)
print(speed)

"""
Error: UnboundLocalError: local variable 'speed' referenced before assignment
Solution: Use the 'global' keyword to modify the global variable inside the function.
"""

# Corrected Code
speed = 60

def increase_speed(increment):
    global speed
    speed += increment

increase_speed(10)
print(speed)

# Example 16
age = 25

def birthday():
    age += 1

birthday()
print(age)

"""
Error: UnboundLocalError: local variable 'age' referenced before assignment
Solution: Use the 'global' keyword to modify the global variable inside the function.
"""

# Corrected Code
age = 25

def birthday():
    global age
    age += 1

birthday()
print(age)

# Example 17
distance = 100

def add_distance(miles):
    distance += miles

add_distance(50)
print(distance)

"""
Error: UnboundLocalError: local variable 'distance' referenced before assignment
Solution: Use the 'global' keyword to modify the global variable inside the function.
"""

# Corrected Code
distance = 100

def add_distance(miles):
    global distance
    distance += miles

add_distance(50)
print(distance)

# Example 18
points = 0

def add_points(new_points):
    points += new_points

add_points(5)
print(points)

"""
Error: UnboundLocalError: local variable 'points' referenced before assignment
Solution: Use the 'global' keyword to modify the global variable inside the function.
"""

# Corrected Code
points = 0

def add_points(new_points):
    global points
    points += new_points

add_points(5)
print(points)

# Example 19
quantity = 10

def reduce_quantity(amount):
    quantity -= amount

reduce_quantity(3)
print(quantity)

"""
Error: UnboundLocalError: local variable 'quantity' referenced before assignment
Solution: Use the 'global' keyword to modify the global variable inside the function.
"""

# Corrected Code
quantity = 10

def reduce_quantity(amount):
    global quantity
    quantity -= amount

reduce_quantity(3)
print(quantity)

# Example 20
height = 180

def grow(increment):
    height += increment

grow(5)
print(height)

"""
Error: UnboundLocalError: local variable 'height' referenced before assignment
Solution: Use the 'global' keyword to modify the global variable inside the function.
"""

# Corrected Code
height = 180

def grow(increment):
    global height
    height += increment

grow(5)
print(height)