def is_palindrome(num):
    """
    Check whether a given integer number is a palindrome.
    
    Args:
        num: An integer to check
        
    Returns:
        True if the number is a palindrome, False otherwise
    """
    # Convert to string and remove negative sign if present
    num_str = str(abs(num))
    
    # Check if the string reads the same forwards and backwards
    return num_str == num_str[::-1]


# Test cases
if __name__ == "__main__":
    test_cases = [121, 123, -121, 0, 1, 1221, 12321, 12345]
    
    for num in test_cases:
        result = is_palindrome(num)
        print(f"is_palindrome({num}) = {result}")
