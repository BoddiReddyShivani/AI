def check_even_or_odd(num):
    """
    Determine whether a given number is even or odd.
    
    Args:
        num: A value to be checked
        
    Returns:
        "Even" if the number is even, "Odd" if the number is odd
        
    Raises:
        TypeError: If num is not an integer
    """
    # Validate input type - must be integer, not boolean
    if not isinstance(num, int) or isinstance(num, bool):
        raise TypeError(f"Input must be an integer, got {type(num).__name__}")
    
    # Check if even or odd (works with negative numbers too)
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"


# Test cases
if __name__ == "__main__":
    # Valid test cases
    test_cases = [8, 15, 0, -4, -7, 1, 2, 100, 999]
    
    print("Even or Odd Checker:")
    print("-" * 50)
    
    print("Valid inputs:")
    for num in test_cases:
        result = check_even_or_odd(num)
        print(f"Input: {num:4d} → Output: {result}")
    
    # Invalid input handling
    print("\n" + "-" * 50)
    print("Invalid inputs:")
    invalid_cases = [3.5, "8", None, [15], True]
    
    for invalid_input in invalid_cases:
        try:
            result = check_even_or_odd(invalid_input)
            print(f"Input: {invalid_input} → Output: {result}")
        except TypeError as e:
            print(f"Input: {invalid_input} → Error: {e}")
