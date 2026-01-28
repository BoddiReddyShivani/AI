

def format_name(full_name):
    """
    Format a full name into "Last, First" format.
    
    Args:
        full_name (str): The full name (e.g., "John Smith")
        
    Returns:
        str: The formatted name (e.g., "Smith, John")
    """
    parts = full_name.split()
    if len(parts) >= 2:
        last_name = parts[-1]
        first_name = ' '.join(parts[:-1])
        return f"{last_name}, {first_name}"
    else:
        return full_name

# Sample Inputs and Outputs
if __name__ == "__main__":
    test_cases = ["John Smith", "Anita Rao", "James Bond", "Mary Jane Watson"]
    
    print("Full Name Formatting")
    print("=" * 30)
    for name in test_cases:
        formatted = format_name(name)
        print(f"{name} → {formatted}")