"""Functions to help play and score a game of blackjack.

How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""


from typing import Literal, Tuple, Union


def value_of_card(card: str) -> int:
    """Determine the scoring value of a card.

    Args:
        card: given card.

    Returns:
        value of a given card. See below for values:
            1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
            2.  'A' (ace card) = 1
            3.  '2' - '10' = numerical value.
    """
    if card in {"J", "Q", "K"}:
        return 10

    if card == "A":
        return 1

    return int(card)


def higher_card(card_one: str, card_two: str) -> Union[str, Tuple]:
    """Determine which card has a higher value in the hand.

    Args:
        card_one: first card to compare.
        card_two: second card dealt in hand.

    Returns:
        resulting Tuple contains both cards if they are of equal value.
    """
    c_one = value_of_card(card_one)
    c_two = value_of_card(card_two)

    if c_one == c_two:
        return card_one, card_two

    return (card_one, card_two)[c_one < c_two]


def value_of_ace(card_one: str, card_two: str) -> Literal[1, 11]:
    """Calculate the most advantageous value for the ace card.

    Values of cards:
        1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
        2.  'A' (ace card) = 11 (if already in hand)
        3.  '2' - '10' = numerical value.

    Args:
        card_one: first card in hand.
        card_two: second card in hand.

    Returns:
        value of the upcoming ace card.
    """
    # Here value of ace is 11.
    _value_of_card = lambda card: (11, value_of_card(card))[card != "A"]

    if _value_of_card(card_one) + _value_of_card(card_two) > 10:
        return 1

    return 11


def is_blackjack(card_one: str, card_two: str) -> bool:
    """Determine if the hand is a 'natural' or 'blackjack'.

    Args:
        card_one: first card in hand.
        card_two: second card in hand.

    Returns:
        is the hand a blackjack (two cards worth 21)?
    """
    value_10_cards = {"K", "Q", "J", "10"}

    return "A" in {card_one, card_two} and (
        card_one in value_10_cards or card_two in value_10_cards
    )


def can_split_pairs(card_one: str, card_two: str) -> bool:
    """Determine if a player can split their hand into two hands.

    Args:
        card_one: first card in hand.
        card_two: second card in hand.

    Returns:
        can the hand be split into two pairs? (i.e. cards are of the same value).
    """
    return value_of_card(card_one) == value_of_card(card_two)


def can_double_down(card_one: str, card_two: str) -> bool:
    """Determine if a blackjack player can place a double down bet.

    Args:
        card_one: first card in hand.
        card_two: second card in hand.

    Returns:
        can the hand can be doubled down? (i.e. totals 9, 10 or 11 points).
    """
    return value_of_card(card_one) + value_of_card(card_two) in {9, 10, 11}
