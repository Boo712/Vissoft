import os

def reverse_file(file_path):

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        reversed_content = content[::-1]
        new_file_path = os.path.join(os.path.dirname(file_path), "reversed.txt")
        with open(new_file_path, 'w', encoding='utf-8') as new_file:
            new_file.write(reversed_content)
        print(f"Reversed content has been saved to: {new_file_path}")

    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    file_path = input("Enter the file path: ")
    reverse_file(file_path)