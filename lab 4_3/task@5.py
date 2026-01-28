def count_lines(filename):
    # Open the file in read mode
    with open(filename, "r") as file:
        # Read all lines from the file and store them in a list
        lines = file.readlines()
    
    # Return the total number of lines in the file
    return len(lines)

