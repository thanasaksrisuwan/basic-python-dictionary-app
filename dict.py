import json

# Load the dictionary data
def load_dictionary():
    with open("dictionary.json") as file:
        data = json.load(file)
        return data

# Search for a word in the dictionary
def search_word(word, dictionary):
    word = word.lower()
    if word in dictionary:
        return dictionary[word]
    else:
        return "Word not found in the dictionary."

# Main function
def main():
    dictionary = load_dictionary()
    while True:
        word = input("Enter a word (or 'q' to quit): ")
        if word == 'q':
            break
        result = search_word(word, dictionary)
        print(result)

# Entry point of the application
if __name__ == "__main__":
    main()
