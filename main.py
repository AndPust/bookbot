# print("hello world")

def print_content(content):
    print(content)


def count_words(content):
    return len(content.split())


def count_letters(content):
    alphabet = {chr(x):0 for x in range(97, 123)}

    for c in content:
        if c.isalpha():
            alphabet[c.lower()] += 1

    return alphabet

def letter_report(letter_dict):
    for alpha in letter_dict:
        print(f"The '{alpha}' character was found {letter_dict[alpha]} times")


def main():
    with open("./books/frankenstein.txt", "r") as f:
        content = f.read()
        print_content(content)
        # n_words = count_words(content)
        print(f"The contents have {count_words(content)} words.")
        print(count_letters(content))
        letter_report(count_letters(content))


main()