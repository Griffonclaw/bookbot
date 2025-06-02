def num_words(text):
    words = text.split()
    count = len(words)
    return count

def character_count(book):
    char_convert = book.lower()
    char_count = {}
    for character in char_convert:
        if character in char_count:
            char_count[character] += 1
        else:
            char_count[character] = 1
    return char_count

def sort_on(dict):
    return dict["num"]

# Seperate each character into is own dictionary and sort them from greatest to least
def dict_sort(book):

    original_dict = book
    list_of_dicts = []
    for char, num in original_dict.items():
        list_of_dicts.append({"char": char, "num": num})
        

    list_of_dicts.sort(reverse=True, key=sort_on)
    
    return list_of_dicts
    