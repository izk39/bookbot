# Counts each individual word in the file.
def wcount_text(string):
    ws = string.split()
    wcount = 0
    for w in ws:
        wcount += 1
    print(f"Found {wcount} total words")


def letter_counter(text):
    chars = list(text.lower())
    char_count = {}
    for c in chars:
        char_count[c] = char_count.get(c, 0) + 1
    print(char_count)
    return char_count
