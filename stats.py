def count_words(file_content):
    words = file_content.split()
    return len(words)

def count_characters(Text):
    text = Text.lower()
    character_count = {}

    for character in text:
        if character not in character_count:
           character_count[character] = 1
        else: character_count[character] += 1

    return character_count

def sort_list(dictionary):
    list_of_dictionaries = []
    for entry in dictionary:
        current_entry = {"char": entry, "num": dictionary[entry]}
        list_of_dictionaries.append(current_entry)

    list_of_dictionaries.sort(reverse=True, key=sort_on)

    return list_of_dictionaries

def sort_on(count):
    return count["num"]

