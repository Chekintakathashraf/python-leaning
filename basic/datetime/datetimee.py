# ===================== Part 1: Introduction to the `datetime` Module =====================

import datetime

# ===================== Example 1: Getting the Current Date and Time =====================
# The `datetime.now()` function returns the current local date and time as a `datetime` object.
current_datetime = datetime.datetime.now()
print(f"Current date and time: {current_datetime}")
# Output will vary depending on the current date and time

# ===================== Example 2: Working with Date and Time Components =====================
# Extracting individual components from the `datetime` object (year, month, day, hour, minute, second).
current_datetime = datetime.datetime.now()

print(f"Year: {current_datetime.year}")
print(f"Month: {current_datetime.month}")
print(f"Day: {current_datetime.day}")
print(f"Hour: {current_datetime.hour}")
print(f"Minute: {current_datetime.minute}")
print(f"Second: {current_datetime.second}")
# Example Output:
# Year: 2025
# Month: 2
# Day: 3
# Hour: 14
# Minute: 25
# Second: 55

# ===================== Example 3: Creating Specific `datetime` Objects =====================
# Creating a specific `datetime` object using the constructor (year, month, day, hour, minute, second).
specific_datetime = datetime.datetime(2022, 5, 10, 14, 30, 0)
print(f"Specific datetime: {specific_datetime}")
# Output: Specific datetime: 2022-05-10 14:30:00

# ===================== Example 4: Getting the Current Date and Time Separately =====================
# Extracting date and time separately from the current `datetime` object.
current_date = datetime.date.today()  # Gets only the date (year, month, day)
current_time = datetime.datetime.now().time()  # Gets only the time (hour, minute, second)

print(f"Current date: {current_date}")
print(f"Current time: {current_time}")
# Example Output:
# Current date: 2025-02-03
# Current time: 14:25:55.203218

# ===================== Practice Questions =====================
# 1. Print the current date and time in the format `DD/MM/YYYY HH:MM:SS`.

current_datetime = datetime.datetime.now()
formatted_datetime = current_datetime.strftime("%d/%m/%Y %H:%M:%S")
print(f"Formatted current date and time: {formatted_datetime}")
# Example Output: Formatted current date and time: 03/02/2025 14:25:55

# 2. Create a `datetime` object for your birthday (use an example date, such as 1st January 2000).
birthday = datetime.datetime(2000, 1, 1, 0, 0, 0)
print(f"My birthday: {birthday}")
# Output: My birthday: 2000-01-01 00:00:00

# 3. Find the number of days between today and a specific past date (e.g., January 1, 2000).
past_date = datetime.datetime(2000, 1, 1)
today = datetime.datetime.now()
difference = today - past_date
print(f"Difference in days: {difference.days}")
# Example Output: Difference in days: 9125

# 4. Convert a date string ("2025-02-03") into a `datetime` object and print it.
date_str = "2025-02-03"
date_object = datetime.datetime.strptime(date_str, "%Y-%m-%d")
print(f"Parsed datetime object: {date_object}")
# Output: Parsed datetime object: 2025-02-03 00:00:00

# Creating a specific time object: 14:30:00 (2:30 PM)
specific_time = datetime.time(14, 30, 0)
print(f"Specific time: {specific_time}")
# Output: Specific time: 14:30:00

# ===================== Example 2: Extracting Components from a `time` Object =====================
# Extracting hour, minute, and second from a `time` object
specific_time = datetime.time(14, 30, 0)

print(f"Hour: {specific_time.hour}")
print(f"Minute: {specific_time.minute}")
print(f"Second: {specific_time.second}")
# Example Output:
# Hour: 14
# Minute: 30
# Second: 0
