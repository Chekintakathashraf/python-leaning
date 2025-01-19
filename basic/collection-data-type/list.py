# Examples for list methods

# 1. append()
my_list = [1, 2, 3]
my_list.append(4)
# my_list is now [1, 2, 3, 4]

# 2. extend()
my_list = [1, 2, 3]
my_list.extend([4, 5])
# my_list is now [1, 2, 3, 4, 5]

# 3. insert()
my_list = [1, 2, 3]
my_list.insert(1, 1.5)
# my_list is now [1, 1.5, 2, 3]

# 4. remove()
my_list = [1, 2, 3, 4]
my_list.remove(3)
# my_list is now [1, 2, 4]

# 5. pop()
my_list = [1, 2, 3, 4]
popped_element = my_list.pop()
# popped_element is 4, my_list is now [1, 2, 3]

# 6. clear()
my_list = [1, 2, 3, 4]
my_list.clear()
# my_list is now []

# 7. index()
my_list = [1, 2, 3, 4]
index_of_3 = my_list.index(3)
# index_of_3 is 2

# 8. count()
my_list = [1, 2, 3, 3, 4]
count_of_3 = my_list.count(3)
# count_of_3 is 2

# 9. sort()
my_list = [4, 2, 3, 1]
my_list.sort()
# my_list is now [1, 2, 3, 4]

# 10. reverse()
my_list = [1, 2, 3, 4]
my_list.reverse()
# my_list is now [4, 3, 2, 1]

# 11. copy()
my_list = [1, 2, 3, 4]
my_list_copy = my_list.copy()
# my_list_copy is [1, 2, 3, 4]


# Examples of loops in a list

# 1. Using a for loop to iterate over the list
my_list = [1, 2, 3, 4]
for item in my_list:
    print(item)
# Output: 1 2 3 4

# 2. Using a while loop to iterate over the list
my_list = [1, 2, 3, 4]
i = 0
while i < len(my_list):
    print(my_list[i])
    i += 1
# Output: 1 2 3 4

# 3. Using list comprehension to iterate over the list
my_list = [1, 2, 3, 4]
squared_list = [item ** 2 for item in my_list]
print(squared_list)
# Output: [1, 4, 9, 16]