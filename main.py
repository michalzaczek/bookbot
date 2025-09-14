def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()


def count_words(text):
    return len(text.split())


def main():
    frankenstein_text = get_book_text("books/frankenstein.txt")
    num_words = count_words(frankenstein_text)
    print(f"{num_words} words found in the document")


main()
