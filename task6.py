from task3 import string_info

def read_file(file_path):

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        length, word_count, char_count = string_info(content)
        print(f"String length: {length}")
        print(f"Number of words: {word_count}")
        print(f"Number of characters (excluding spaces): {char_count}")

    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    file_path = input("Enter the file path: ")
    read_file(file_path)