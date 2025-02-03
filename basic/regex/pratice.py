import re

# ===================== Module 1 =====================

# 1. **Basic Regex Patterns**  
# Matching any character except newline with `.`
text = "a.b"
match = re.match(r"a.b", text)  # Matches: "acb", "a1b", "a-b"
if match:
    print(f"Match found: {match.group()}")  # Output: a.b

# 2. **Anchors: `^` (start of string) and `$` (end of string)**
text = "Hello World"
match = re.match(r"^Hello", text)  # Checks if the string starts with 'Hello'
print(match.group())  # Output: Hello

# 3. **Quantifiers: `*`, `+`, `?`, `{n}`, `{n,m}`**
text = "abbbb"
match = re.match(r"ab*", text)  # Matches 'a' followed by zero or more 'b's
print(match.group())  # Output: abbbb

# 4. **Character Classes: `\d`, `\w`, `\s`**
text = "My number is 123"
match = re.search(r"\d+", text)  # Find one or more digits
print(match.group())  # Output: 123

# ===================== Module 2 =====================

# 1. **Using `re.match()` to match at the start of a string**
text = "Hello World"
match = re.match(r"Hello", text)
if match:
    print("Match found:", match.group())  # Output: Hello

# 2. **Using `re.search()` to search anywhere in the string**
text = "I love Python programming."
match = re.search(r"Python", text)
if match:
    print("Match found:", match.group())  # Output: Python

# 3. **Using `re.findall()` to find all matches**
text = "I have 2 apples, 3 bananas, and 5 oranges."
numbers = re.findall(r"\d+", text)
print("Numbers found:", numbers)  # Output: ['2', '3', '5']

# 4. **Using `re.finditer()` to find all matches as an iterator**
text = "The cat sat on the mat."
matches = re.finditer(r"\b\w{3}\b", text)  # 3-letter words
for match in matches:
    print(f"Match: {match.group()}, Position: {match.start()}")  
# Output: Match: cat, Position: 4
# Output: Match: sat, Position: 8
# Output: Match: mat, Position: 19

# 5. **Using `re.sub()` for substitution**
text = "My phone number is 123-456-7890."
new_text = re.sub(r"\d", "X", text)
print("Replaced text:", new_text)  # Output: My phone number is XXX-XXX-XXXX.

# 6. **Using `re.split()` to split text using regex pattern**
text = "apple, banana; orange|grape"
words = re.split(r"[;,|]", text)
print("Words:", words)  # Output: ['apple', ' banana', ' orange', 'grape']

# 7. **Using Flags for case-insensitive matching**
text = "Hello World"
match = re.search(r"hello", text, re.IGNORECASE)  # Case insensitive
print("Match found:", match.group())  # Output: Hello

# ===================== Module 3 =====================

# 1. **Lookahead - Positive Lookahead**
text = "Python 3 is fun, Python 2 is old."
matches = re.findall(r"Python(?=\s3)", text)  # Match 'Python' followed by space and '3'
print("Matches:", matches)  # Output: ['Python']

# 2. **Lookahead - Negative Lookahead**
text = "I love Python 3, but not Python 2."
matches = re.findall(r"Python(?!\s2)", text)  # Match 'Python' not followed by space and '2'
print("Matches:", matches)  # Output: ['Python']

# 3. **Lookbehind - Positive Lookbehind**
text = "I have Python 3 book and a Python 2 book."
matches = re.findall(r"(?<=Python\s)3", text)  # Match '3' preceded by 'Python '
print("Matches:", matches)  # Output: ['3']

# 4. **Lookbehind - Negative Lookbehind**
text = "I have Python 3, but not Python 2."
matches = re.findall(r"(?<!Python\s)3", text)  # Match '3' not preceded by 'Python '
print("Matches:", matches)  # Output: ['3']

# 5. **Non-Greedy Matching**
text = "<h1>Title</h1> <h2>Subtitle</h2>"
greedy_match = re.findall(r"<h.*>.*</h.*>", text)  # Greedy match
non_greedy_match = re.findall(r"<h.*?>.*?</h.*?>", text)  # Non-greedy match
print(f"Greedy match: {greedy_match}")
print(f"Non-greedy match: {non_greedy_match}")
# Output: Greedy match: ['<h1>Title</h1> <h2>Subtitle</h2>']
# Output: Non-greedy match: ['<h1>Title</h1>', '<h2>Subtitle</h2>']

# ===================== Module 4 =====================

# 1. **Backreferences Example**
text = "Hello Hello, How are you?"
matches = re.findall(r"(\b\w+\b) \1", text)  # Match repeated words
print("Repeated Words:", matches)  # Output: ['Hello']

# 2. **Using `re.sub()` for Complex Substitution**
text = "The event is on 12-05-2025 and the meeting is on 13-05-2025."
new_text = re.sub(r"(\d{2})-(\d{2})-(\d{4})", r"\3-\2-\1", text)  # Change date format
print("Replaced text:", new_text)  # Output: The event is on 2025-05-12 and the meeting is on 2025-05-13.

# 3. **Combining Multiple Patterns (Email or Phone Number)**
text = "Contact me at support@example.com or 123-456-7890."
pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}|(\d{3}-\d{3}-\d{4})"
matches = re.findall(pattern, text)
print("Matches:", matches)  # Output: ['support@example.com', '123-456-7890']

# ===================== Practice Questions =====================

# 1. **Validate US Phone Number (123-456-7890)**
phone_pattern = r"\d{3}-\d{3}-\d{4}"
phone_numbers = ["123-456-7890", "1234567890", "123-45-6789"]
for phone in phone_numbers:
    if re.match(phone_pattern, phone):
        print(f"{phone} is valid.")
    else:
        print(f"{phone} is invalid.")
# Output: 123-456-7890 is valid. 1234567890 is invalid. 123-45-6789 is invalid.

# 2. **Extract all hashtags from a tweet**
tweet = "Learning #Python is fun! #coding #AI"
hashtags = re.findall(r"#\w+", tweet)
print("Hashtags:", hashtags)  # Output: ['#Python', '#coding', '#AI']

# 3. **Validate Date Format (DD/MM/YYYY or MM-DD-YYYY)**
date_pattern = r"(\d{2})[-/](\d{2})[-/](\d{4})"
dates = ["12/05/2025", "13-06-2025", "2025-12-05"]
for date in dates:
    if re.match(date_pattern, date):
        print(f"{date} is valid.")
    else:
        print(f"{date} is invalid.")
# Output: 12/05/2025 is valid. 13-06-2025 is valid. 2025-12-05 is invalid.

# 4. **Validate Credit Card Number (1234 5678 1234 5678)**
credit_card_pattern = r"\d{4} \d{4} \d{4} \d{4}"
credit_cards = ["1234 5678 1234 5678", "1234567812345678", "1234 5678 1234"]
for card in credit_cards:
    if re.match(credit_card_pattern, card):
        print(f"{card} is valid.")
    else:
        print(f"{card} is invalid.")
# Output: 1234 5678 1234 5678 is valid. 1234567812345678 is invalid. 1234 5678 1234 is invalid.
