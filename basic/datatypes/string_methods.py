# capitalize() - Converts the first character to upper case
s = "hello world"
print(s.capitalize())  # Output: "Hello world"

# casefold() - Converts string into lower case
s = "Hello World"
print(s.casefold())  # Output: "hello world"

# center() - Returns a centered string
s = "hello"
print(s.center(10))  # Output: "  hello   "

# count() - Returns the number of times a specified value occurs in a string
s = "hello world"
print(s.count("l"))  # Output: 3

# encode() - Returns an encoded version of the string
s = "hello"
print(s.encode())  # Output: b'hello'

# endswith() - Returns true if the string ends with the specified value
s = "hello world"
print(s.endswith("world"))  # Output: True

# expandtabs() - Sets the tab size of the string
s = "h\te\tl\tl\to"
print(s.expandtabs(2))  # Output: "h e l l o"

# find() - Searches the string for a specified value and returns the position of where it was found
s = "hello world"
print(s.find("world"))  # Output: 6

# format() - Formats specified values in a string
s = "Hello {}"
print(s.format("world"))  # Output: "Hello world"

# format_map() - Formats specified values in a string using a dictionary
s = "Hello {name}"
print(s.format_map({"name": "world"}))  # Output: "Hello world"

# index() - Searches the string for a specified value and returns the position of where it was found
s = "hello world"
print(s.index("world"))  # Output: 6

# isalnum() - Returns True if all characters in the string are alphanumeric
s = "hello123"
print(s.isalnum())  # Output: True

# isalpha() - Returns True if all characters in the string are in the alphabet
s = "hello"
print(s.isalpha())  # Output: True

# isdecimal() - Returns True if all characters in the string are decimals
s = "123"
print(s.isdecimal())  # Output: True

# isdigit() - Returns True if all characters in the string are digits
s = "123"
print(s.isdigit())  # Output: True

# isidentifier() - Returns True if the string is an identifier
s = "hello"
print(s.isidentifier())  # Output: True

# islower() - Returns True if all characters in the string are lower case
s = "hello"
print(s.islower())  # Output: True

# isnumeric() - Returns True if all characters in the string are numeric
s = "123"
print(s.isnumeric())  # Output: True

# isprintable() - Returns True if all characters in the string are printable
s = "hello"
print(s.isprintable())  # Output: True

# isspace() - Returns True if all characters in the string are whitespaces
s = "   "
print(s.isspace())  # Output: True

# istitle() - Returns True if the string follows the rules of a title
s = "Hello World"
print(s.istitle())  # Output: True

# isupper() - Returns True if all characters in the string are upper case
s = "HELLO"
print(s.isupper())  # Output: True

# join() - Joins the elements of an iterable to the end of the string
s = "-"
print(s.join(["hello", "world"]))  # Output: "hello-world"

# ljust() - Returns a left justified version of the string
s = "hello"
print(s.ljust(10))  # Output: "hello     "

# lower() - Converts a string into lower case
s = "HELLO"
print(s.lower())  # Output: "hello"

# lstrip() - Returns a left trim version of the string
s = "   hello"
print(s.lstrip())  # Output: "hello"

# maketrans() - Returns a translation table to be used in translations
s = "hello"
table = s.maketrans("h", "y")
print(s.translate(table))  # Output: "yello"

# partition() - Returns a tuple where the string is parted into three parts
s = "hello world"
print(s.partition(" "))  # Output: ('hello', ' ', 'world')

# replace() - Returns a string where a specified value is replaced with a specified value
s = "hello world"
print(s.replace("world", "there"))  # Output: "hello there"

# rfind() - Searches the string for a specified value and returns the last position of where it was found
s = "hello world world"
print(s.rfind("world"))  # Output: 12

# rindex() - Searches the string for a specified value and returns the last position of where it was found
s = "hello world world"
print(s.rindex("world"))  # Output: 12

# rjust() - Returns a right justified version of the string
s = "hello"
print(s.rjust(10))  # Output: "     hello"

# rpartition() - Returns a tuple where the string is parted into three parts
s = "hello world"
print(s.rpartition(" "))  # Output: ('hello', ' ', 'world')

# rsplit() - Splits the string at the specified separator, and returns a list
s = "hello world"
print(s.rsplit(" "))  # Output: ['hello', 'world']

# rstrip() - Returns a right trim version of the string
s = "hello   "
print(s.rstrip())  # Output: "hello"

# split() - Splits the string at the specified separator, and returns a list
s = "hello world"
print(s.split(" "))  # Output: ['hello', 'world']

# splitlines() - Splits the string at line breaks and returns a list
s = "hello\nworld"
print(s.splitlines())  # Output: ['hello', 'world']

# startswith() - Returns true if the string starts with the specified value
s = "hello world"
print(s.startswith("hello"))  # Output: True

# strip() - Returns a trimmed version of the string
s = "   hello   "
print(s.strip())  # Output: "hello"

# swapcase() - Swaps cases, lower case becomes upper case and vice versa
s = "Hello World"
print(s.swapcase())  # Output: "hELLO wORLD"

# title() - Converts the first character of each word to upper case
s = "hello world"
print(s.title())  # Output: "Hello World"

# translate() - Returns a translated string
s = "hello"
table = s.maketrans("h", "y")
print(s.translate(table))  # Output: "yello"

# upper() - Converts a string into upper case
s = "hello"
print(s.upper())  # Output: "HELLO"

# zfill() - Fills the string with a specified number of 0 values at the beginning
s = "42"
print(s.zfill(5))  # Output: "00042"