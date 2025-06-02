from stats import num_words, character_count, dict_sort
import sys

def get_book_text(path):
    return path


def main():
    # path = "books/frankenstein.txt"
    
    
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    else:
        book_path = sys.argv[1]
        with open(get_book_text(book_path)) as f:
            file_contents = f.read()
            dict_list = character_count(file_contents)
            print(f"============ BOOKBOT ============ \n Analyzing book found at {book_path}...")
            print(f"----------- Word Count ---------- \n Found {num_words(file_contents)} total words")
            print(f"--------- Character Count -------")
            for char in dict_sort(dict_list):
                if char["char"].isalpha():
                    print(f"{char['char']}: {char['num']}")
            print(f"============= END ===============")

main()