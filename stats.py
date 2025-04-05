def count_words(file_contents):
    return len(file_contents.split())


def count_character_occurrence(file_contents):
    char_map = {}

    for c in file_contents.lower():
        if c not in char_map:
            char_map[c] = 0

        char_map[c] += 1

    return char_map
