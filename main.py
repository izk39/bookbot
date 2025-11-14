from stats import letter_counter, wcount_text


# Gets the contents of filepath as a string
def get_book_text(filepath):
    if not isinstance(filepath, str):
        raise TypeError("filepath must be a string")

    with open(filepath) as f:
        file_contents = f.read()

    return file_contents


test = get_book_text("./books/frankenstein.txt")
wcount_text(test)
letter_counter(test)
