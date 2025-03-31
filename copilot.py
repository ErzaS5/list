def sort_list(input_list):
    """Sorts and returns the given list in ascending order."""
    return sorted(input_list)

# Initial list
default_list = [1, 11, 0.11, 9, 3, 87, 1111, 999, 0.011]
print("Default list:", default_list)
print("Sorted default list:", sort_list(default_list))

# Allow user to input a list from a file
file_path = input("\nEnter the path to the file containing a list of numbers: ")

try:
    with open(file_path, 'r') as file:
        # Assume the file contains a list of numbers separated by spaces or newlines
        file_contents = file.read()
        user_list = [float(num) for num in file_contents.split()]  # Convert strings to floats
        print("\nUser-provided list:", user_list)
        print("Sorted user-provided list:", sort_list(user_list))
except FileNotFoundError:
    print("Error: The specified file does not exist.")
except ValueError:
    print("Error: The file contains invalid data. Please ensure it contains only numbers.")
