"""
Python File Handling Functions - Comprehensive Example with Explanation

This script demonstrates various file handling functions in Python,
including opening, reading, writing, and manipulating files.
"""

import os
import json
import csv

# 1. File Opening and Closing
# Open a file in read mode
def open_and_close_file():
    """Opens and closes a file."""
    file = open("example.txt", "r")
    file.close()


# 2. File Reading Functions
def read_file():
    """Reads content from a file."""
    with open("example.txt", "r") as file:
        content = file.read()  # Reads entire file
        first_line = file.readline()  # Reads one line
        all_lines = file.readlines()  # Reads all lines as list
    return content, first_line, all_lines


# 3. File Writing Functions
def write_file():
    """Writes content to a file."""
    with open("example.txt", "w") as file:
        file.write("Hello, World!\n")
        file.writelines(["Line 1\n", "Line 2\n"])


# 4. File Positioning Functions
def file_positioning():
    """Demonstrates seek and tell functions."""
    with open("example.txt", "r") as file:
        file.seek(5)  # Move to the 5th byte
        position = file.tell()  # Get current position
    return position


# 5. File Handling Modes
# Available modes: 'r', 'w', 'a', 'r+', 'w+', 'a+', 'rb', 'wb'

def file_modes_example():
    """Demonstrates different file modes."""
    with open("example.txt", "w") as file:
        file.write("Overwriting content")


# 6. Working with File Attributes
def file_attributes():
    """Displays file attributes."""
    file = open("example.txt", "r")
    info = (file.name, file.mode, file.closed)
    file.close()
    return info


# 7. File Checking and Deletion Functions
def check_and_delete_file():
    """Checks if file exists and deletes it."""
    if os.path.exists("example.txt"):
        os.remove("example.txt")
        return "File deleted"
    return "File not found"


# 8. Using with statement
def with_statement_example():
    """Demonstrates use of 'with' statement to handle files."""
    with open("example.txt", "r") as file:
        content = file.read()
    return content


# 9. Binary File Handling
def binary_file_handling():
    """Reads binary data from an image file."""
    with open("image.jpg", "rb") as file:
        data = file.read()
    return len(data)


# 10. File Encoding
def file_encoding():
    """Reads file with specified encoding."""
    with open("example.txt", "r", encoding="utf-8") as file:
        content = file.read()
    return content


# 11. JSON and CSV File Handling
def json_and_csv_example():
    """Demonstrates reading and writing JSON and CSV files."""
    data = {"name": "Alice", "age": 25}
    with open("data.json", "w") as file:
        json.dump(data, file)

    with open("data.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Age"])
        writer.writerow(["Alice", 25])


if __name__ == "__main__":
    write_file()
    print(read_file())
    print(file_positioning())
    print(file_attributes())
    print(check_and_delete_file())
    json_and_csv_example()
