"""Functions to help edit essay homework using string manipulation."""


def capitalize_title(title: str) -> str:
    """Convert the first letter of each word in the title to uppercase.

    Args:
        title: title string that needs title casing.

    Returns:
        title string in title case (first letters capitalized).
    """
    return title.title()


def check_sentence_ending(sentence: str) -> bool:
    """Check the ending of the sentence to verify that a period is present.

    Args:
        sentence: a sentence to check.

    Returns:
        True if punctuated correctly with period, False otherwise.
    """
    return sentence.endswith(".")


def clean_up_spacing(sentence: str) -> str:
    """Check if there isn't any whitespace at start or end of the sentence.

    Args:
        sentence: sentence to clean of leading and trailing space characters.

    Returns:
        sentence, cleaned of leading and trailing space characters.
    """
    return sentence.strip()


def replace_word_choice(sentence: str, old_word: str, new_word: str) -> str:
    """Replace a word in the provided sentence with a new one.

    Args:
        sentence: a sentence to replace words in.
        old_word: word to replace.
        new_word: replacement word.

    Returns:
        input sentence with new words in place of old words.
    """
    return sentence.replace(old_word, new_word)
