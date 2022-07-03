"""Soultion for `Register Color Duo` exercise."""

from typing import List

from resistor_color import resistor_band


def value(colors: List[str]) -> int:
    """Returns combined value of first two register color band."""
    return resistor_band[colors[0]] * 10 + resistor_band[colors[1]]
