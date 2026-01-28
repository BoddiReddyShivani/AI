def cm_to_inches(centimeters):
    """
    Convert centimeters to inches.
    
    Formula: inches = centimeters / 2.54
    
    Args:
        centimeters (float): The length in centimeters
        
    Returns:
        float: The equivalent length in inches (rounded to 2 decimal places)
    """
    inches = centimeters / 2.54
    return round(inches, 2)


# Sample Test Cases
if __name__ == "__main__":
    test_cases = [10, 5, 25.4, 50, 100, 2.54, 30, 15, 1, 254]

    print("Centimeters to Inches Conversion")
    print("=" * 45)
    print(f"{'Centimeters':<15} | {'Inches':<15}")
    print("-" * 45)

    for cm in test_cases:
        inches = cm_to_inches(cm)
        print(f"{cm:<15} | {inches:<15}")