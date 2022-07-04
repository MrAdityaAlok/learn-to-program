"""This module defines function to calculate score in a dart game."""

from math import sqrt
from typing import Union

_RealNumber = Union[int, float]


def score(x: _RealNumber, y: _RealNumber) -> int:
    """Calculates score of dart game.

    Args:
        x: X - Coordinate of the dart.
        y: Y - Coordinate of the dart.

    Returns:
        Score earned out of 0, 1, 5 or 10.
    """
    distance_from_origin = sqrt(x**2 + y**2)
    score = 10  # Inside inner circle.

    if distance_from_origin > 10:  # Outside target.
        score = 0
    elif distance_from_origin > 5:  # Inside outer circle.
        score = 1
    elif distance_from_origin > 1:  # Inside middle circle.
        score = 5

    return score
