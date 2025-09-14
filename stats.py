def get_num_words(text):
    return len(text.split())


def count_characters(text):
    text_lower = text.lower()
    letters_dict = {}
    for c in text_lower:
        if c.isalpha():
            letters_dict[c] = letters_dict.get(c, 0) + 1

    return letters_dict
