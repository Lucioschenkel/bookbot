def count_words(file_contents):
    return len(file_contents.split())

def count_character_occurrence(file_contents):
    char_map = {}

    for c in file_contents.lower():
        if c not in char_map:
            char_map[c] = 0

        char_map[c] += 1

    return char_map

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
        "z"
    }

    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        word_count = count_words(file_contents)
        char_map = count_character_occurrence(file_contents)

        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{word_count} words found in the document")

        for key in char_map:
            if key in alphabet:
                print(f"The '{key}' character was found {char_map[key]} times")


        print("--- End report ---")

main()
