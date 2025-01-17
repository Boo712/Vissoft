from task2 import calculate_sum
from task3 import string_info
from task4 import word_length_dict

def process_input(input_data):

    if input_data.isdigit():
        n = int(input_data)
        print(f"The sum of numbers from 1 to {n} is: {calculate_sum(n)}")

    else:
        length, word_count, char_count = string_info(input_data)
        print(f"String length: {length}")
        print(f"Number of words: {word_count}")
        print(f"Number of characters (excluding spaces): {char_count}")
        word_dict = word_length_dict(input_data)
        print("Word and length dictionary:")
        print(word_dict)

if __name__ == "__main__":
    input_data = input("Enter a number or a string: ")
    process_input(input_data)