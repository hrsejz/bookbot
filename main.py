def main():
    book_path = "books/frankenstein.txt"
    book_string = get_book_text(book_path)
    word_count = get_num_words(book_string)
    char_count_dict = get_num_char(book_string)
    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document\n")
    print(char_count_dict)
    dict_list = dic_to_list(char_count_dict)
    # print(dict_list)
    print("-----------------------------------------")
    dict_list.sort(reverse=True, key=sort_on)
    # print(dict_list)
    for index in dict_list:
        for key, value in index.items():
            if key.isalpha():
                print(f"The '{key}' character was found {value} times")
    print("--- End report ---")


def sort_on(item):
    return list(item.values())[0]


def dic_to_list(dictionary):
    dict_list = []
    for key in dictionary:
        dic = {key: dictionary[key]}
        dict_list.append(dic)
    return dict_list


def get_num_char(text):
    lowered_text = text.lower()
    freq = {}
    for c in lowered_text:
        if c in freq:
            freq[c] += 1
        else:
            freq[c] = 1
    return dict(freq)


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()


# def main():
#     with open("books/frankenstein.txt") as f:
#         file_contents = f.read()
#         print(file_contents)

#     def number_of_words():
#         words = file_contents.split()
#         word_count = len(word)
#         print(word_count)

#     number_of_words()
# main()
