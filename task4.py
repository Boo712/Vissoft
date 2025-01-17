def word_length_dict(string):
    word_dict = {word: len(word) for word in string.split()}
    return word_dict

if __name__ == "__main__":
    string = input("Enter a string: ")
    word_dict = word_length_dict(string)
    print("Word and length dictionary:")
    print(word_dict)