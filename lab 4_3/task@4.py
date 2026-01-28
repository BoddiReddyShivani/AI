


def count_vowels(text):
    """
    Count the number of vowels in a given string.
    
    Vowels are: a, e, i, o, u (both lowercase and uppercase)
    
    Args:
        text (str): The input string
        
    Returns:
        int: The total count of vowels in the string
    """
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count
