# Example 1: Reading the entire file content
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)

# Example 2: Reading the file line by line using readline()
with open('example.txt', 'r') as file:
    line = file.readline()
    while line:
        print(line, end='')
        line = file.readline()

# Example 3: Reading all lines into a list using readlines()
with open('example.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        print(line, end='')

# Example 4: Reading a text file
with open('textfile.txt', 'r') as file:
    content = file.read()
    print(content)

# Example 5: Reading a video file (binary mode)
with open('video.mp4', 'rb') as file:
    content = file.read()
    print(content[:100])  # Print first 100 bytes

# Example 6: Reading an audio file (binary mode)
with open('audio.mp3', 'rb') as file:
    content = file.read()
    print(content[:100])  # Print first 100 bytes

# Example 7: Reading a file and converting content to int
with open('numbers.txt', 'r') as file:
    numbers = [int(line.strip()) for line in file]
    print(numbers)

# Example 8: Reading a file and converting content to float
with open('floats.txt', 'r') as file:
    floats = [float(line.strip()) for line in file]
    print(floats)

# Example 9: Reading a file with 'r+' mode (read and write)
with open('example.txt', 'r+') as file:
    content = file.read()
    print(content)
    file.write('\nNew line added.')

# Example 10: Reading and writing simultaneously
with open('example.txt', 'r+') as file:
    content = file.read()
    print(content)
    file.seek(0)
    file.write('Overwritten content\n')

# Example 11: Reading a file in chunks
with open('example.txt', 'r') as file:
    while chunk := file.read(1024):
        print(chunk)

# Example 12: Reading a file using a context manager
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)

# Example 13: Reading a file without using a context manager
file = open('example.txt', 'r')
try:
    content = file.read()
    print(content)
finally:
    file.close()

# Example 14: Reading a file and handling exceptions
try:
    with open('example.txt', 'r') as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("File not found")

# Example 15: Reading a file with a specific encoding
with open('example.txt', 'r', encoding='utf-8') as file:
    content = file.read()
    print(content)

# Example 16: Reading a file and stripping whitespace
with open('example.txt', 'r') as file:
    lines = [line.strip() for line in file]
    print(lines)

# Example 17: Reading a file and counting lines
with open('example.txt', 'r') as file:
    line_count = sum(1 for line in file)
    print(f'Number of lines: {line_count}')

# Example 18: Reading a file and counting words
with open('example.txt', 'r') as file:
    word_count = sum(len(line.split()) for line in file)
    print(f'Number of words: {word_count}')

# Example 19: Reading a file and counting characters
with open('example.txt', 'r') as file:
    char_count = sum(len(line) for line in file)
    print(f'Number of characters: {char_count}')

# Example 20: Reading a file and finding a specific word
with open('example.txt', 'r') as file:
    found = any('specific_word' in line for line in file)
    print(f'Word found: {found}')