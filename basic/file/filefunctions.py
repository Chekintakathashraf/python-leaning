import os

# Open a file
file = open('example.txt', 'w')

# Write to a file
file.write('Hello, world!')

# Close a file
file.close()

# Read from a file
file = open('example.txt', 'r')
content = file.read()
print(content)
file.close()

# Append to a file
file = open('example.txt', 'a')
file.write('\nAppending a new line.')
file.close()

# Read lines from a file
file = open('example.txt', 'r')
lines = file.readlines()
for line in lines:
    print(line.strip())
file.close()

# Using 'with' statement to handle file operations
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)

# Check if a file exists
if os.path.exists('example.txt'):
    print('File exists')
else:
    print('File does not exist')

# Delete a file
if os.path.exists('example.txt'):
    os.remove('example.txt')
    print('File deleted')
else:
    print('File does not exist')