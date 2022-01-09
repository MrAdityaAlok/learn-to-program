from collections import Counter


def find_anagrams(word, candidates):
    word = word.lower()
    # Counter is faster than sorting
    word_count = Counter(word)
    return [
        candidate
        for candidate in candidates
        if candidate.lower() != word and word_count == Counter(candidate.lower())
    ]
