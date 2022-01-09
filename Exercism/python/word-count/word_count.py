from re import findall
from collections import Counter


def count_words(sentence):
    return Counter(
        findall("[a-z0-9]+'[st]|[a-z0-9]+", sentence.lower()),
    )
