"""Utility program to help in cooking lasagna.

This module defines Utility functions to help in cooking lasagna.
"""

EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2


def bake_time_remaining(elapsed_bake_time: int) -> int:
    """Calculates the bake time remaining.

    Takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to
    bake based on the `EXPECTED_BAKE_TIME`.

    Args:
        elapsed_bake_time:
            Count of baking time already elapsed.

    Returns:
        Remaining bake time derived from 'EXPECTED_BAKE_TIME'.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time


def preparation_time_in_minutes(num_of_layers: int) -> int:
    """Calculates the time needed to make layers of lasagna.

    Args:
        num_of_layers:
            Number of layers to be added to lasagna.

    Returns:
        How many minutes is needed to make `num_of_layers` lasagna layers.
    """
    return num_of_layers * PREPARATION_TIME


def elapsed_time_in_minutes(num_of_layers: int, elapsed_bake_time: int) -> int:
    """Calculates the total amount of time you have been cooking.

    Args:
        num_of_layers:
            Number of layers added to lasagna.
        elapsed_bake_time:
             Number of minutes the lasagna has been baking in the oven.

    Returns:
        How much amount of time you have spent on cooking.
    """
    return preparation_time_in_minutes(num_of_layers) + elapsed_bake_time
