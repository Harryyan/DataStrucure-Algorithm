def removeChars(str, remove):
    char_flags = {}
    for r in remove:
        char_flags[r] = True
