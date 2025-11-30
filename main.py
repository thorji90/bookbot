import sys

from stats import count_words
from stats import count_characters
from stats import sort_list

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) == 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    file_contents = get_book_text(sys.argv[1])
    word_count = count_words(file_contents)
    characters = count_characters(file_contents)
    char_list = sort_list(characters)
    print("============ BOOKBOT ============")
    print("Analyzing book found at " + sys.argv[1])
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for entry in char_list:
        if entry["char"].isalpha():
            print(f"{entry["char"]}: {entry["num"]}")

main()    

