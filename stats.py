# Counts each individual word in the file.
def wcount_text(string):
    ws = string.split()
    wcount = 0
    for w in ws:
        wcount += 1
    print(f"Found {wcount} total words")
