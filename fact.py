def factorial(n):
    """
    Calculate the factorial of a given non-negative integer.
    
    Args:
        n: A non-negative integer
        
    Returns:
        The factorial of n
        
    Raises:
        TypeError: If n is not an integer
        ValueError: If n is negative
    """
    # Handle invalid input types
    if not isinstance(n, int) or isinstance(n, bool):
        raise TypeError(f"Input must be a non-negative integer, got {type(n).__name__}")
    
    # Handle negative numbers
    if n < 0:
        raise ValueError(f"Input must be non-negative, got {n}")
    
    # Base case: 0! = 1
    if n == 0 or n == 1:
        return 1
    
    # Calculate factorial using iteration
    result = 1
    for i in range(2, n + 1):
        result *= i
    
    return result


# Test cases
if __name__ == "__main__":
    # Valid test cases
    test_cases = [0, 1, 5, 10]
    
    print("Valid inputs:")
    for num in test_cases:
        result = factorial(num)
        print(f"factorial({num}) = {result}")    
    # Invalid input handling
    print("\nInvalid inputs:")
    invalid_cases = [(-5, "got -5"), (3.5, "got float"), ("5", "got str")]
    
    for invalid_input, error_part in invalid_cases:
        try:
            result = factorial(invalid_input)
            print(f"factorial({invalid_input}) = {result}")
        except (TypeError, ValueError) as e:
            print(f"factorial({invalid_input}) → Error: {e}")