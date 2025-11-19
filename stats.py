def get_num_words(text):
    words = text.split()
    return len(words)

def get_num_letters(text):
    text = text.lower()
    word_count = {}

    for letter in text:
        if letter in word_count:
            word_count[letter] += 1
        else:
            word_count[letter] = 1

    return word_count

def format_dictionary(d):
    new_list = []
    for item in d:
        if item.isalpha():  # only keep alphabetic characters
            new_list.append({"char": item, "num": d[item]})
    return sorted(new_list, key=lambda x: x["num"], reverse=True)
