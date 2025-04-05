import sys
from stats import count_words, count_character_occurrence


def main():
    alphabet = {
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
    }

    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    with open(book_path) as f:
        file_contents = f.read()
        word_count = count_words(file_contents)
        char_map = count_character_occurrence(file_contents)

        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{word_count} words found in the document")

        for key in char_map:
            if key in alphabet:
                print(f"{key}: {char_map[key]}")

        print("--- End report ---")


main()
