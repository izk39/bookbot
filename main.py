# Gets the contents of filepath as a string
def get_book_text(filepath):
    if not isinstance(filepath, str):
        raise TypeError("filepath must be a string")

    with open(filepath) as f:
        file_contents = f.read()
        print(file_contents)


get_book_text("./books/frankenstein.txt")
