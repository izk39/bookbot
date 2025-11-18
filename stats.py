# Counts each individual word in the file.
def wcount_text(string):
    ws = string.split()
    wcount = 0
    for w in ws:
        wcount += 1

    return wcount


def letter_counter(text):
    chars = list(text.lower())
    char_count = {}
    for c in chars:
        char_count[c] = char_count.get(c, 0) + 1
    return char_count


# Function for sorting dictionary key-value pairs into keys with the greatest value. Returns a list
# of dictionaries containing the following structure: [{"char" : @ , "num" : 123}]


def dict_sort(dict):
    sorted_list = sorted(dict.items(), key=lambda i: i[1], reverse=True)
    char_num = [{"char": c, "num": n} for c, n in sorted_list]
    char_num_alpha = [i for i in char_num if i["char"].isalpha()]

    return char_num_alpha
