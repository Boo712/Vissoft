csv_file_path = "pokemon.csv"

def show_menu():
    print("\n=== Main Menu ===")
    print("1: Print 'Hello, world!'")
    print("2: Calculate the sum of numbers from 1 to n")
    print("3: Get string information (length, word count, character count)")
    print("4: Create a dictionary of words and their lengths")
    print("5: Process input (number or string)")
    print("6: Read file and get string information")
    print("7: Reverse content of a file")
    print("8: Create JSON files for Pokemon")
    print("9: Find Pokemon by ID or name")
    print("10: Export Pokemon data matching a keyword to CSV")
    print("0: Exit the program")
    print("=================")

if __name__ == "__main__":
    while True:
        show_menu()
        choice = input("Enter task number to run (or 0 to exit): ")
        if choice == "0":
            print("Goodbye!")
            break
        try:
            if choice in {"8", "9", "10"}:
                exec(open(f"task{choice}.py").read())
            else:
                exec(open(f"task{choice}.py").read())
        except FileNotFoundError:
            print("Task file not found.")
        except Exception as e:
            print(f"An error occurred: {e}")