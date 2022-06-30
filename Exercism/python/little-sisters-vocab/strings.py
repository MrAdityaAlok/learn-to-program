"""Functions for creating, transforming, and adding prefixes to strings."""


from typing import List, Literal, Union


def add_prefix_un(word: str) -> str:
    """Take the given word and add the 'un' prefix.

    Args:
        word: containing the root word.

    Returns:
        root word prepended with 'un'.
    """
    return f"un{word}"


def make_word_groups(vocab_words: List[str]) -> Union[str, Literal[""]]:
    """Prepend a prefix to given list of words.


    This function takes a `vocab_words` list and returns a string
    with the prefix and the words with prefix applied, separated
    by ' :: '.

    For example:
        list('en', 'close', 'joy', 'lighten'), produces the following string:
            'en :: enclose :: enjoy :: enlighten'.

    Args:
        vocab_words: list of vocabulary words with prefix in first index.

    Returns:
        prefix followed by vocabulary words with prefix applied.
    """
    if not vocab_words:
        return ""

    prefix = vocab_words[0]
    return (
        f"{prefix} ::"
        f" {' :: '.join(map(lambda word: f'{prefix}{word}', vocab_words[1:]))}"
    )


def remove_suffix_ness(word: str) -> str:
    """Remove the suffix from the word while keeping spelling in mind.

    For example:
        "heaviness" becomes "heavy", but "sadness" becomes "sad".

    Args:
        word: word to remove suffix from.

    Returns:
        word with suffix removed & spelling adjusted.
    """
    root = word[:-4]
    if root[-1].lower() == "i" and root[-2].lower() not in "aeiou":
        root = root[:-1] + "y"

    return root


def adjective_to_verb(sentence: str, index: int) -> str:
    """Change the adjective within the sentence to a verb.

    For example:
        ("It got dark as the sun set", 2) becomes "darken".

    Args:
        sentence: sentence whoes within adjective is to be changed.
        index: index of the word to remove and transform.

    Returns:
        word that changes the extracted adjective to a verb.
    """
    return f"{sentence.replace('.','').split()[index]}en"
