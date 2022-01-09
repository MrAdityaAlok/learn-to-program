"""This module implements the Luhn algorithm.

It is used to check validity of various identification numbers.
For example: credit card number, Canadian Social Insurance Numbers,
survey codes on MacDonald and Taco Bell, etc.

Note: It is not intended to be a cryptographically secure hash
function; it was designed to protect against accidental errors,
not malicious attacks.
"""


class Luhn:  # supress too-few public methods warning; pylint: disable=R0903
    """check validity of various identification numbers using Luhn algorithm.

    Attributes:
        card_num: string representing identification number,
            i.e the number to be verified.
    """

    def __init__(self, card_num: str) -> None:
        """Initalize Luhn with identification number.

        Args:
            card_num: number to be verified
        """
        self.card_num = card_num
        self._is_valid = self._validate(
            stripped_num=self.card_num.replace(" ", "")[::-1]
        )

    @staticmethod
    def _validate(stripped_num: str) -> bool:
        """Validates identification number.

        Args:
            stripped_num: card_num but reversed and devoid
                of spaces.
        """
        if len(stripped_num) <= 1 or not stripped_num.isdecimal():
            return False

        sum_ = 0
        for i, digit in enumerate(stripped_num, start=1):
            digit = int(digit)
            if i % 2 == 0:
                mul = digit * 2
                sum_ += mul - 9 if mul > 9 else mul
            else:
                sum_ += digit
        return sum_ % 10 == 0

    def valid(self) -> bool:
        """Returns whether identification number is valid or not."""
        return self._is_valid
