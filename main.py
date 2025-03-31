def sort_list(data):
  """Sorts a given list of numbers."""
  return sorted(data)
def load_list_from_file(filepath):
  """Loads a list of numbers from a file. Args: filepath: The path to the file containing the list.
  Returns:A list of numbers, or None if an error occurred."""
  try:
      # Read the entire file content as a string
    with open(filepath, 'r') as file:
      content = file.read()
      # Remove leading/trailing whitespace and split by commas or spaces
      numbers_str = content.strip().replace(" ", ",").split(',')
      # Attempt to convert each string to a float; ignore empty strings.
      numbers = [float(num) for num in numbers_str if num]
      return numbers
  except FileNotFoundError:
    print(f"Error: File '{filepath}' not found.")
    return None
  except ValueError:
      print(f"Error: File '{filepath}' contains invalid number format.")
      return None
  except Exception as e:
    print(f"An unexpected error occurred: {e}")
    return None
def main():
  """Main function to handle list sorting."""
  default_list = [1, 11, 0.11, 9, 3, 87, 1111, 999, 0.011]
  print("Default list:", default_list)
  sorted_default = sort_list(default_list)
  print("Sorted default list:", sorted_default)
  use_file = input("Do you want to load a list from a file? (yes/no): ").lower()
  if use_file == "yes":
    filepath = input("Enter the file path: ")
    loaded_list = load_list_from_file(filepath)
    if loaded_list:
      sorted_loaded = sort_list(loaded_list)
      print("Sorted list from file:", sorted_loaded)
  elif use_file == "no":
      print("Exiting.")
  else:
      print("Invalid input. Please enter 'yes' or 'no'.")
if __name__ == "__main__":
  main()

