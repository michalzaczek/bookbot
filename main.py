from stats import count_characters, get_num_words, get_sorted_letters
import sys


def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()


def main():
    # BOOK_FILE_PATH = "books/frankenstein.txt"
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    BOOK_FILE_PATH = sys.argv[1]

    frankenstein_text = get_book_text(BOOK_FILE_PATH)
    num_words = get_num_words(frankenstein_text)
    counted_characters = count_characters(frankenstein_text)
    sorted_letters = get_sorted_letters(counted_characters)
    letter_lines = "\n".join(f"{letter}: {count}" for letter, count in sorted_letters)

    print_text = f"""
============ BOOKBOT ============
Analyzing book found at {BOOK_FILE_PATH}...
----------- Word Count ----------
Found {num_words} total words
--------- Character Count -------
{letter_lines}
============= END ===============
"""

    print(print_text)


main()
