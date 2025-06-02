from stats import num_words, character_count, dict_sort

def get_book_text(path):
    return f"{path}"

def main():
    path = "books/frankenstein.txt"
    with open(get_book_text(path)) as f:
        file_contents = f.read()
        # print(f"{num_words(file_contents)} words found in the document")
        # print(f"{character_count(file_contents)}")
        print(dict_sort(file_contents))
main()
