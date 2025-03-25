import sys
from stats import (
    get_number_of_words,
    get_number_of_chars,
    sort_dict
)


def get_book_text(filepath: str) -> str:
    with open(filepath) as f:
        file_content = f.read()
        return file_content

def print_report(book_path, word_count, sorted_chars) -> None:
    print("========== BOOKBOT ==========")
    print(f"Analyzing book found at {book_path}...")
    print("---------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("---------- Character Count ----------")
    for item in sorted_chars:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")
    print("========== END ==========")


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        exit(1)

    book_path = sys.argv[1]
    raw_text = get_book_text(book_path)
    word_count = get_number_of_words(raw_text)
    char_count = sort_dict(get_number_of_chars(raw_text))

    print_report(book_path, word_count, char_count)

if __name__ == "__main__":
    main()
