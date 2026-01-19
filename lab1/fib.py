# Program to print Fibonacci sequence up to n terms

# Take user input for the number of terms
n = int(input("Enter the number of terms: "))

# Initialize the first two Fibonacci numbers
a = 0
b = 1

# Print the Fibonacci sequence
if n <= 0:
    print("Please enter a positive number")
elif n == 1:
    print(a)
else:
    # Print first two terms
    print(a)
    print(b)
    
    # Generate and print remaining terms
    for i in range(2, n):
        c = a + b  # Calculate next Fibonacci number
        print(c)
        a = b      # Update a to the next number
        b = c      # Update b to the newest number
