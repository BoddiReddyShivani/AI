# Program to check if a year is a leap year
# Leap year rules:
# 1. If divisible by 400, it is a leap year
# 2. If divisible by 100, it is not a leap year
# 3. If divisible by 4, it is a leap year
# 4. Otherwise, it is not a leap year

# Get year input from user
year = int(input("Enter a year: "))

# Check using basic conditional logic
if year % 400 == 0:
    # If divisible by 400, it's definitely a leap year
    print(f"{year} is a leap year")
elif year % 100 == 0:
    # If divisible by 100 but not 400, it's not a leap year
    print(f"{year} is not a leap year")
elif year % 4 == 0:
    # If divisible by 4 but not 100, it's a leap year
    print(f"{year} is a leap year")
else:
    # All other years are not leap years
    print(f"{year} is not a leap year")
