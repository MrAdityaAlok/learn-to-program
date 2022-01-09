from re import match


def is_valid(isbn):
    _match = match(r"^(\d)-?(\d{3,3})-?(\d{5,5})-?([\dX])$", isbn)
    if _match:
        groups = _match.groups()
        parsed_isbn = list("".join(groups[0:3])) + [
            (groups[3], "10")[groups[3] == "X"]
        ]
        return (
            sum(int(parsed_isbn[10 - i]) * i for i in range(10, 0, -1)) % 11
            == 0
        )
    return False
