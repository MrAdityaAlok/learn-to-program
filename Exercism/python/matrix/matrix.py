from typing import List


class Matrix:
    def __init__(self, matrix_string: str):
        """An utility class for matrix."""
        self._matrix: List[List[int]] = [
            [int(element) for element in matrix_row.split()]
            for matrix_row in matrix_string.splitlines()
        ]

    def row(self, index: int) -> List[int]:
        if index < 1:
            raise IndexError("No such row")
        return self._matrix[index - 1].copy()

    def column(self, index: int) -> List[int]:
        # this loops through every row and returns list of repective column element
        if index < 1:
            raise IndexError("No such column")
        return [matrix_row[index - 1] for matrix_row in self._matrix]
