from stats import sort_dict, word_count, char_count
import sys


def get_book_text(path: str):
    file_contents = ""
    with open(path) as f:
        file_contents = f.read()
    return file_contents


def report(word_count: int, path: str, dic: dict[str, int]):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for c in dic:
        print(f"{c}: {dic[c]}")


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        path = sys.argv[1]
        count = word_count(get_book_text(path))
        c_count = sort_dict(char_count(get_book_text(path)))
        report(count, path, c_count)


main()
