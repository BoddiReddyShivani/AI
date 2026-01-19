def is_armstrong_number(num):
    """
    Check whether a given number is an Armstrong number.
    An Armstrong number is equal to the sum of its digits raised to the power of the number of digits.
    
    Args:
        num: An integer to check
        
    Returns:
        "Armstrong Number" if num is an Armstrong number, "Not an Armstrong Number" otherwise
    """
    # Convert to string to get digits
    num_str = str(abs(num))
    num_digits = len(num_str)
    
    # Calculate sum of digits raised to the power of number of digits
    sum_of_powers = sum(int(digit) ** num_digits for digit in num_str)
    
    # Check if it's an Armstrong number
    if sum_of_powers == abs(num):
        return "Armstrong Number"
    else:
        return "Not an Armstrong Number"


# Test cases
if __name__ == "__main__":
    test_cases = [153, 370, 123, 9474, 100, 1, 0]
    
    print("Armstrong Number Checker:")
    for num in test_cases:
        result = is_armstrong_number(num)
        print(f"Input: {num} → Output: {result}")
