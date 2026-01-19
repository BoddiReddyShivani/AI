import math


def classify_number(num):
    """
    Classify a given number as Prime, Composite, or Neither Prime nor Composite.
    
    Args:
        num: A value to be classified
        
    Returns:
        A string classification: "Prime", "Composite", or "Neither Prime nor Composite"
        
    Raises:
        TypeError: If num is not an integer
    """
    # Validate input type
    if not isinstance(num, int) or isinstance(num, bool):
        raise TypeError(f"Input must be an integer, got {type(num).__name__}")
    
    # Handle numbers less than or equal to 1
    if num <= 1:
        return "Neither Prime nor Composite"
    
    # Handle number 2 (only even prime)
    if num == 2:
        return "Prime"
    
    # Handle even numbers (all even numbers > 2 are composite)
    if num % 2 == 0:
        return "Composite"
    
    # Optimize: Check divisibility only up to sqrt(num)
    sqrt_num = int(math.sqrt(num))
    
    # Check odd divisors from 3 to sqrt(num)
    for i in range(3, sqrt_num + 1, 2):
        if num % i == 0:
            return "Composite"
    
    # If no divisors found, it's prime
    return "Prime"


# Test cases
if __name__ == "__main__":
    test_cases = [1, 2, 3, 4, 5, 10, 11, 17, 20, 25, 29, 97, 100, 0, -5]
    
    print("Number Classification:")
    print("-" * 50)
    
    for num in test_cases:
        result = classify_number(num)
        print(f"Input: {num:4d} → Output: {result}")
    
    # Invalid input handling
    print("\n" + "-" * 50)
    print("Invalid inputs:")
    invalid_cases = [3.5, "17", None, [5]]
    
    for invalid_input in invalid_cases:
        try:
            result = classify_number(invalid_input)
            print(f"Input: {invalid_input} → Output: {result}")
        except TypeError as e:
            print(f"Input: {invalid_input} → Error: {e}")
