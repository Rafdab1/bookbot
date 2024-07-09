
book_path = "books/frankenstein.txt"

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    count = {}
    text = text.lower()
    for character in text:
        if character in count:
            count[character] += 1
        else:
            count[character] = 1
    return count

def sort_on(dict):
    return dict["num"]

def chars_dict_to_sorted_list(dict):
    sorted_list =[]
    for character in dict:
        sorted_list.append({"char": character, "num": dict[character]})
        sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def generate_report(word_count,list_of_dict):
    print(f"--- Begin report of {book_path} ---\n")
    print(f"{word_count} words found in the document\n")
    for ch in list_of_dict:
        if ch['char'].isalpha():
            print(f"The '{ch['char']}' character was found {ch['num']} times")

    print("\n--- End report ---")

def main ():
    book_text = get_book_text(book_path)
    words_num = count_words(book_text)
    print(words_num)
    generate_report(words_num,chars_dict_to_sorted_list(count_characters(book_text)))
main()