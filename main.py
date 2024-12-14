def main():
    book_path = "books/frankenstein.txt"
    book_string = get_book_text(book_path)
    word_count = get_num_words(book_string)
    print(f"Number of words in the book: {word_count}")

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