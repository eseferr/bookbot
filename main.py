import string
def main():
        book_path="./books/frankenstein.txt"
        text = get_book_text(book_path)
        print_report(text)
       
#Open and read the book
def get_book_text(path):
    with open(path) as f:
        return f.read()
#Count words on books
def count_words(text):
    return len(text.split())

#Number of times each character appears in the book
def character_appeared(text):
    character_dictionary = {}
    text = list(text.lower())
    alphabet = list(string.ascii_lowercase)
    for i in text:
        if i in character_dictionary and i in alphabet:
            character_dictionary[i] +=1
        elif i in alphabet:
             character_dictionary[i] = 1
    sorted_characters = sorted(character_dictionary.items(), key=lambda item: item[1], reverse=True)
    return sorted_characters
#Print Report
def print_report(text):
    print("---------------- BOOK REPORT ----------------\n")
    print(f"Words found in the book: {count_words(text)}\n")
    characters = character_appeared(text)
    for char, count in characters:
         print(f"The {char} character was found {count} times")
    print("\n---------------- END ----------------")

main()