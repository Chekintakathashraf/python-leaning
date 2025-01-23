import os

# Renaming a file
def rename_file(old_name, new_name):
    try:
        os.rename(old_name, new_name)
        print(f"File renamed from {old_name} to {new_name}")
    except FileNotFoundError:
        print(f"The file {old_name} does not exist")
    except Exception as e:
        print(f"An error occurred: {e}")

# Deleting a file
def delete_file(file_name):
    try:
        os.remove(file_name)
        print(f"File {file_name} deleted")
    except FileNotFoundError:
        print(f"The file {file_name} does not exist")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
if __name__ == "__main__":
    rename_file('old_file.txt', 'new_file.txt')
    delete_file('new_file.txt')

