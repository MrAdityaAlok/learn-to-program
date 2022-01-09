from math import log10


def factors_within_limit(__min: int, __max: int, num: int) -> list:
    factors = []
    _sqrt = int(num ** 0.5)

    for i in range(__min, (__max, _sqrt)[_sqrt < __max] + 1):
        div = num // i
        if not num % i and i <= div <= __max:
            factors.append((i, div))
    return factors


def all_digits(num: str, check: str) -> bool:
    if check == "1":
        if not num[0] == num[-1] == "1":
            return False
        num = num[1:-1]
        check = "0"

    for d in num:
        if d != check:
            return False

    return True


def mirror(num: int, __advance: bool = False, __next: bool = False) -> int:
    length = int(log10(num) + 1)
    diff = (0, (-1, 1)[__next])[__advance]

    if length == 1:
        return num + diff

    mul = 10 ** (length // 2)
    first_half = num // mul + diff

    second_half = (
        first_half // 10 ** ((int(log10(first_half)) + 1) // 2)
        if length % 2
        else first_half
    )

    return first_half * mul + int(str(second_half)[::-1])


def advance(palin: int, __next: bool, __convert: bool = False) -> int:
    new_palin = 0  # init

    if __convert:
        num_str = str(palin)
        new_palin = palin if num_str == num_str[::-1] else mirror(palin)
        while (new_palin < palin, new_palin > palin)[__next]:
            new_palin = advance(new_palin, __next=(not __next and new_palin < palin))

    elif __next and all_digits(str(palin), "9"):  # match(r"^9+$", str(palin)):
        new_palin = palin + 2
    elif not __next and all_digits(str(palin), "1"):  # match(r"^10+1$", str(palin)):
        new_palin = palin - 2
    elif not __next and palin == 11:
        new_palin = 9
    else:
        new_palin = mirror(palin, __advance=True, __next=__next)

    return new_palin


def palindrome(__min: int, __max: int, __largest: bool = False) -> tuple:
    if __min > __max or __min < 1:
        raise ValueError("could not calculate palindrome for given arguments")

    __min_limit, __max_limit = __min ** 2, __max ** 2
    limit = (__min_limit, __max_limit)[__largest]

    palin = advance(limit, __next=__largest, __convert=True)

    while __min_limit <= palin <= __max_limit:
        factors = factors_within_limit(__min, __max, palin)
        if factors:
            return palin, factors

        palin = advance(palin, __next=not __largest)

    return None, []


def largest(max_factor: int, min_factor: int = 0) -> tuple:
    return palindrome(min_factor, max_factor, __largest=True)


def smallest(max_factor: int, min_factor: int = 0) -> tuple:
    return palindrome(min_factor, max_factor)
