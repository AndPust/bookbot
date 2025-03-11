# print("hello world")

from stats import get_num_words
import sys

def print_content(content):
    print(content)




def count_letters(content):
    alphabet = {chr(x):0 for x in range(97, 123)}

    for c in content:
        if c.isalpha() and c.lower() in alphabet:
            alphabet[c.lower()] += 1

    return alphabet

def letter_report(letter_dict):
    for alpha in letter_dict:
        print(f"{alpha}: {letter_dict[alpha]}")


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    path = sys.argv[1]

    if len(path) < 1:
        path = "./books/frankenstein.txt"

    with open(path, "r") as f:
        content = f.read()
        print_content(content)
        # n_words = count_words(content)
        print(f"{get_num_words(content)} words found in the document")
        print(count_letters(content))
        letter_report(count_letters(content))


main()