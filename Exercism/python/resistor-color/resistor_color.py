"""Soultion for `Register Color` exercise."""

from typing import List, Union

resistor_band = {
    "black": 0,
    "brown": 1,
    "red": 2,
    "orange": 3,
    "yellow": 4,
    "green": 5,
    "blue": 6,
    "violet": 7,
    "grey": 8,
    "white": 9,
}


def color_code(color: str) -> Union[int, None]:
    """Returns code for corresponding resistor color in color band.

    Args:
        color: Color whose code is to be returned.
    """
    return resistor_band.get(color)


def colors() -> List[str]:
    """Returns list of all color in resistor's color band."""
    return list(resistor_band)
