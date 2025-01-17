def string_info(string):
    length = len(string)
    word_count = len(string.split())
    char_count = len("".join(string.split()))
    return length, word_count, char_count

if __name__ == "__main__":
    string = input("Enter a string: ")
    length, word_count, char_count = string_info(string)
    print(f"String length: {length}")
    print(f"Number of words: {word_count}")
    print(f"Number of characters (excluding spaces): {char_count}")