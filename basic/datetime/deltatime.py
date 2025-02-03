

# Create a fixed time zone with UTC+2
import datetime

utc_offset = datetime.timedelta(hours=2)
timezone = datetime.timezone(utc_offset)

# Get the current time in UTC+2
current_time = datetime.datetime.now(timezone)
print(f"Current time in UTC+2: {current_time}")
# Output: Current time in UTC+2: 2025-02-03 16:00:00+02:00

# ===================== Example 2: Converting Between Time Zones =====================
utc_time = datetime.datetime.now(datetime.timezone.utc)
utc_plus_three = datetime.timezone(datetime.timedelta(hours=3))

# Convert UTC time to UTC+3
converted_time = utc_time.astimezone(utc_plus_three)
print(f"Converted time (UTC+3): {converted_time}")
# Output: Converted time (UTC+3): 2025-02-03 17:00:00+03:00

# ===================== Part 6: Advanced Formatting and Parsing =====================

# ===================== Example 1: Formatting `datetime` Objects with `strftime` =====================
current_datetime = datetime.datetime.now()
formatted_datetime = current_datetime.strftime("%d/%m/%Y %H:%M:%S")
print(f"Formatted current date and time: {formatted_datetime}")
# Example Output: Formatted current date and time: 03/02/2025 14:25:55

# ===================== Example 2: Parsing Strings to `datetime` with `strptime` =====================
date_str = "03/02/2025 14:25:55"
parsed_datetime = datetime.datetime.strptime(date_str, "%d/%m/%Y %H:%M:%S")
print(f"Parsed datetime object: {parsed_datetime}")
# Example Output: Parsed datetime object: 2025-02-03 14:25:55

# ===================== Part 7: Working with Timestamps and Advanced Date Arithmetic =====================

# ===================== Example 1: Converting `datetime` to Unix Timestamp =====================
current_datetime = datetime.datetime.now()
timestamp = current_datetime.timestamp()
print(f"Current timestamp: {timestamp}")
# Example Output: Current timestamp: 1735791155.203218

# ===================== Example 2: Converting Unix Timestamp to `datetime` =====================
timestamp = 1735791155.203218
datetime_object = datetime.datetime.fromtimestamp(timestamp)
print(f"Datetime from timestamp: {datetime_object}")
# Example Output: Datetime from timestamp: 2025-02-03 14:25:55.203218

# ===================== Example 3: Advanced Date Arithmetic with `timedelta` =====================
current_datetime = datetime.datetime.now()
ten_days = datetime.timedelta(days=10)

# Adding 10 days to the current datetime
new_datetime = current_datetime + ten_days
print(f"New datetime after adding 10 days: {new_datetime}")

# Subtracting 10 days from the current datetime
new_datetime_subtract = current_datetime - ten_days
print(f"New datetime after subtracting 10 days: {new_datetime_subtract}")
# Example Output:
# New datetime after adding 10 days: 2025-02-13 14:25:55.203218
# New datetime after subtracting 10 days: 2025-01-24 14:25:55.203218
