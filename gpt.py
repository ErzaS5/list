def sort_and_print(numbers):
    sorted_list = sorted(numbers)
    print("Sorted list:", sorted_list)

def read_list_from_file(filename):
    try:
        with open(filename, 'r') as f:
            line = f.readline()
            # Convert string values to float
            numbers = [float(x.strip()) for x in line.split(',')]
            return numbers
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    except ValueError:
        print("The file should contain only numbers, separated by commas.")
    return None

def gpt():
    # Default list
    default_list = [1, 11, 0.11, 9, 3, 87, 1111, 999, 0.011]
    print("Default list:", default_list)
    sort_and_print(default_list)

    # Ask user for input file
    user_input = input("\nWould you like to sort a list from a file? (y/n): ").strip().lower()
    if user_input == 'y':
        filename = input("Enter the filename: ").strip()
        numbers_from_file = read_list_from_file(filename)
        if numbers_from_file is not None:
            print("List from file:", numbers_from_file)
            sort_and_print(numbers_from_file)

if __name__ == "__main__":
    gpt()
