# Gets the contents of filepath as a string
def get_book_text(filepath):
    if not isinstance(filepath, str):
        raise TypeError("filepath must be a string")

    with open(filepath) as f:
        file_contents = f.read()

    return file_contents


test = get_book_text("./books/frankenstein.txt")


# Counts each individual word in the file.
def wcount_text(string):
    ws = string.split()
    wcount = 0
    for w in ws:
        wcount += 1
    print(f"Found {wcount} total words")


wcount_text(test)
