
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
    return list(dict.values())[0]

def generate_report(word_count,character_dict):
    #preparing for report
    list_of_dict = []
    for character in character_dict:
        if character.isalpha():
            list_of_dict.append({character: character_dict[character]})

    list_of_dict.sort(reverse=True ,key=sort_on)

    #pirnting report
    print (f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document\n")
    for dict in list_of_dict:
        print(f"The { list(dict.keys())[0] } character was found { list(dict.values())[0] } times")
    print("\n--- End report ---")



def main ():
    book_text = get_book_text(book_path)
    words_num = count_words(book_text)
    print(words_num)
    generate_report(words_num,count_characters(book_text))
main()