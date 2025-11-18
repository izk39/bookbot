from stats import dict_sort, letter_counter, wcount_text


# Gets the contents of filepath as a string
def get_book_text(filepath):
    if not isinstance(filepath, str):
        raise TypeError("filepath must be a string")

    with open(filepath) as f:
        file_contents = f.read()

    return file_contents


test = get_book_text("./books/frankenstein.txt")


def report(filepath):
    print("============ BOOKBOT ============\n", f"Analyzing book found at {filepath}")
    print("----------- Word Count ----------")
    text = get_book_text(filepath)
    text_count = wcount_text(text)
    print(f"Found {text_count} total words")
    print("--------- Character Count -------")
    ccount = letter_counter(text)
    sorted_ccount = dict_sort(ccount)
    for i in sorted_ccount:
        print(f"{i['char']}: {i['num']}")
    print("============= END ===============")


report("./books/frankenstein.txt")
