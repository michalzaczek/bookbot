from stats import count_characters, get_num_words


def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()


def main():
    frankenstein_text = get_book_text("books/frankenstein.txt")
    num_words = get_num_words(frankenstein_text)
    print(f"{num_words} words found in the document")
    print(count_characters(frankenstein_text))


main()
