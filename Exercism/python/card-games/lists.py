"""Functions for tracking poker hands and assorted card tasks.

Python list documentation: https://docs.python.org/3/tutorial/datastructures.html
"""


from typing import List


def get_rounds(number: int) -> List[int]:
    """Create a list containing the current and next two round numbers.

    Args:
        number: current round number.

    Returns:
        current round and the two that follow.
    """
    return list(range(number, number + 3))


def concatenate_rounds(rounds_1: List[int], rounds_2: List[int]):
    """Concatenate two lists of round numbers.

    Args:
        rounds_1: first rounds played.
        rounds_2: second set of rounds played.

    Returns:
        all rounds played.
    """
    return [*rounds_1, *rounds_2]


def list_contains_round(rounds: List[int], number: int) -> bool:
    """Check if the list of rounds contains the specified number.

    Args:
        rounds: rounds played.
        number: round number.

    Returns:
        was the round played?
    """
    return number in rounds


def card_average(hand: List[int]) -> float:
    """Calculate and returns the average card value from the list.

    Args:
        hand: cards in hand.

    Returns:
        average value of the cards in the hand.
    """
    return sum(hand) / len(hand)


def approx_average_is_average(hand: List[int]) -> bool:
    """Check if approx average is equal to actual average.

    Approx average is calculated using:
        1. first + last index values  OR
        2. 'middle' card.

    Args:
        hand: cards in hand.

    Returns:
        does one of the approximate averages equal the `true average`?
    """
    calc_avg = card_average(hand)

    if (
        card_average([hand[0], hand[-1]]) == calc_avg
        or hand[len(hand) // 2] == calc_avg
    ):
        return True

    return False


def average_even_is_average_odd(hand: List) -> bool:
    """Return if (avg of even indexed values) == (avg of odd indexed values).

    Args:
        hand: cards in hand.

    Returns:
        are even and odd averages equal?
    """
    odd_index_values = []
    even_index_values = []

    for index, value in enumerate(hand):
        if index % 2 == 0:
            even_index_values.append(value)
        else:
            odd_index_values.append(value)

    return card_average(even_index_values) == card_average(odd_index_values)


def maybe_double_last(hand: List[int]) -> List[int]:
    """Multiply a Jack card value in the last index position by 2.

    Args:
        hand: list of cards in hand.

    Returns:
        hand with Jacks (if present) value doubled.
    """
    if hand[-1] == 11:
        hand[-1] = 22

    return hand
