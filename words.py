"""print each word, uppercased.
"""
def print_upper_words(words):
    for word in words:
        print(word.upper())

"""Print each word, uppercased if itstarts with "e" or "E"
"""

def print_upper_words2(words):
    for word in words:
        if word.startswith("e") or word.startswith("E"):
            print(word.upper())


"""Print each word, uppercased, if it starts with a given letter
"""

def print_upper_words3(words,must_start_with):
    for word in words:
        for letter in must_start_with:
            if word.startswith(letter):
                print(word.upper())
                break
