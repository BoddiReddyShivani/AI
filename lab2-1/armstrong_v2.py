# Alternative Armstrong Number Checker - Version 2
# Using mathematical extraction of digits instead of string conversion

# Get user input
number = int(input("Enter a number: "))

# Store original for final comparison
original = number

# Extract total number of digits using mathematical approach
digit_count = 0
temp = number
while temp > 0:
    digit_count += 1
    temp //= 10

# Calculate sum of each digit raised to the power of digit count
sum_result = 0
temp = number

# Extract digits one by one using modulo and division
while temp > 0:
    last_digit = temp % 10              # Extract last digit
    sum_result += last_digit ** digit_count  # Add powered digit to sum
    temp //= 10                         # Remove last digit

# Verify if number is Armstrong
if sum_result == original:
    print(f"{original} is an Armstrong number!")
else:
    print(f"{original} is not an Armstrong number")
