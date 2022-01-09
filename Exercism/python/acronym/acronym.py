from re import findall


def abbreviate(words):
    return "".join(
        [w[0].upper() for w in findall(r"([A-Za-z])[A-Za-z']*", words)]
    )
