def is_isogram(string: str):
    """Check if a sentence or word is an isogram or not."""
    read_chars = []  # read letters
    for ch in string.lower():
        if ch.isalpha():
            if ch in read_chars:  # check if char pre exist in list
                return False
            read_chars.append(ch)
    return True
