# Program to check if a number is an Armstrong number
# An Armstrong number is a number that equals the sum of its digits each raised to the power of the number of digits
# Example: 153 = 1^3 + 5^3 + 3^3

# Take user input
num = int(input("Enter a number: "))

# Store the original number for comparison
original_num = num

# Convert number to string to easily access each digit
num_str = str(num)

# Count the total number of digits
num_digits = len(num_str)

# Initialize sum variable to store the sum of powered digits
sum_of_powers = 0

# Loop through each digit and calculate the sum of powers
for digit in num_str:
    # Convert digit string to integer and raise it to the power of total digits
    sum_of_powers += int(digit) ** num_digits

# Check if the calculated sum equals the original number
if sum_of_powers == original_num:
    print(f"{original_num} is an Armstrong number")
else:
    print(f"{original_num} is not an Armstrong number")
