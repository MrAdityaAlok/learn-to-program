"""Solution for `Bob` exercise."""


def response(hey_bob: str) -> str:
    hey_bob = hey_bob.strip()

    if not hey_bob:
        return "Fine. Be that way!"

    if hey_bob.isupper():
        if hey_bob.endswith("?"):
            return "Calm down, I know what I'm doing!"

        return "Whoa, chill out!"

    if hey_bob.endswith("?"):
        return "Sure."

    return "Whatever."
