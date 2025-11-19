import sys
from stats import get_num_words, get_num_letters, format_dictionary

def get_book_text(path):
    with open(path) as f:
        file_content = f.read()
        return file_content

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    text = get_book_text(book_path)

    # print("Found " + str(get_num_words(text)) + " total words")
    total_words=get_num_words(text)
    leters_dictionary = get_num_letters(text)
    formated_list = format_dictionary(leters_dictionary)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {total_words} total words")
    print('--------- Character Count -------')
    for i in formated_list:
        # print(i)
        print(f"{i["char"]}: {i["num"]}")
    print("============= END ===============")
main()