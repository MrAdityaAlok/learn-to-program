"Solution for `Leap Year` exercise."


def leap_year(year: int) -> bool:
    """Checks if an year is leap year or not.

    Args:
        year: Year to be checked to be leap year.
    """
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
