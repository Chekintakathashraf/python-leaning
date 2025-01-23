# Writing to a file using 'w' mode (write mode)
with open('example_w.txt', 'w') as file:
    file.write('This is written using write mode.\n')

# Writing to a file using 'a' mode (append mode)
with open('example_a.txt', 'a') as file:
    file.write('This is appended using append mode.\n')

# Writing to a file using 'x' mode (exclusive creation mode)
try:
    with open('example_x.txt', 'x') as file:
        file.write('This is written using exclusive creation mode.\n')
except FileExistsError:
    print('File already exists.')

# Writing to a file using 'b' mode (binary mode)
with open('example_b.bin', 'wb') as file:
    file.write(b'This is written using binary mode.\n')

# Writing to a file using 'w+' mode (write and read mode)
with open('example_w_plus.txt', 'w+') as file:
    file.write('This is written using write and read mode.\n')
    file.seek(0)
    print(file.read())

# Writing to a file using 'a+' mode (append and read mode)
with open('example_a_plus.txt', 'a+') as file:
    file.write('This is appended using append and read mode.\n')
    file.seek(0)
    print(file.read())

# Writing to a file using 'x+' mode (exclusive creation and read mode)
try:
    with open('example_x_plus.txt', 'x+') as file:
        file.write('This is written using exclusive creation and read mode.\n')
        file.seek(0)
        print(file.read())
except FileExistsError:
    print('File already exists.')

# Writing to a file using 'wb' mode (write binary mode)
with open('example_wb.bin', 'wb') as file:
    file.write(b'This is written using write binary mode.\n')

# Writing to a file using 'ab' mode (append binary mode)
with open('example_ab.bin', 'ab') as file:
    file.write(b'This is appended using append binary mode.\n')

# Writing to a file using 'xb' mode (exclusive creation binary mode)
try:
    with open('example_xb.bin', 'xb') as file:
        file.write(b'This is written using exclusive creation binary mode.\n')
except FileExistsError:
    print('File already exists.')

# Writing to a file using 'w+b' mode (write and read binary mode)
with open('example_wb_plus.bin', 'w+b') as file:
    file.write(b'This is written using write and read binary mode.\n')
    file.seek(0)
    print(file.read())

# Writing to a file using 'a+b' mode (append and read binary mode)
with open('example_ab_plus.bin', 'a+b') as file:
    file.write(b'This is appended using append and read binary mode.\n')
    file.seek(0)
    print(file.read())