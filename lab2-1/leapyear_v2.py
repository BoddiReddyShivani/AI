# Optimized Leap Year Checker - Version 2
# Using concise boolean logic for better readability

# Get year input from user
year = int(input("Enter a year: "))

# Leap year logic using compound boolean expression:
# A year is a leap year if:
# - It's divisible by 400, OR
# - It's divisible by 4 AND NOT divisible by 100
is_leap_year = (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)

# Display the result
if is_leap_year:
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")
