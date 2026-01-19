def is_perfect_number(num):
    """
    Check whether a given number is a perfect number.
    A perfect number is equal to the sum of its proper divisors (excluding itself).
    
    Examples:
        6 is perfect: 1 + 2 + 3 = 6
        28 is perfect: 1 + 2 + 4 + 7 + 14 = 28
        10 is not perfect: 1 + 2 + 5 = 8
    
    Args:
        num: An integer to check
        
    Returns:
        True if the number is a perfect number, False otherwise
    """
    # Perfect numbers must be positive and greater than 1
    if num <= 1:
        return False
    
    # Find sum of proper divisors
    divisor_sum = 0
    
    # Check divisors from 1 to sqrt(num) for efficiency
    i = 1
    while i * i <= num:
        if num % i == 0:
            # Add the divisor
            if i != num:  # Exclude the number itself
                divisor_sum += i
            
            # Add the corresponding divisor (num/i)
            # Make sure we don't count the square root twice
            other_divisor = num // i
            if other_divisor != i and other_divisor != num:
                divisor_sum += other_divisor
        
        i += 1
    
    # Check if sum of divisors equals the number
    return divisor_sum == num


# Test cases
if __name__ == "__main__":
    test_cases = [1, 6, 28, 496, 8128, 10, 20, 100, 0, -6]
    
    print("Perfect Number Checker:")
    print("-" * 50)
    
    for num in test_cases:
        result = is_perfect_number(num)
        status = "Perfect Number" if result else "Not a Perfect Number"
        print(f"Input: {num:6d} → Output: {result:5} ({status})")
