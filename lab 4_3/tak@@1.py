def is_leap_year(year):
    """
    Check whether the given year is a leap year.
    
    A year is a leap year if:
    - It is divisible by 4 AND
    - If it is divisible by 100, it must also be divisible by 400
    
    Args:
        year (int): The year to check
        
    Returns:
        bool: True if the year is a leap year, False otherwise
    """
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False


# Sample input and output
if __name__ == "__main__":
    test_years = [2020, 2021, 2000, 1900, 2024, 2019]
    
    for year in test_years:
        result = is_leap_year(year)
        print(f"Year {year}: {result} {'(Leap Year)' if result else '(Not a Leap Year)'}")
