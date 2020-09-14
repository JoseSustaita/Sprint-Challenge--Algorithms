'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word):

    # If word is less than 2, it does not contain
    if len(word) < 2:
        return 0

# If first two letters are th return 1 contain with the other letters
    if word[:2] == "th":
        return 1 + count_th(word[2:])

# Otherwise continue with next letter
    else:
        return count_th(word[1:])

    pass
