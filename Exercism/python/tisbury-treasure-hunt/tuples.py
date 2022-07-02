"""Functions to help Azara and Rui locate pirate treasure."""


from typing import Literal, Tuple, Union


def get_coordinate(record: Tuple) -> str:
    """Returns coordinate value containing the treasure name, and coordinate.

    Args:
        record: with a (treasure, coordinate) pair.

    Returns:
        the extracted map coordinate.
    """
    return record[1]


def convert_coordinate(coordinate: str) -> Tuple[str, str]:
    """Split given coordinate into tuple containing its individual components.

    Args:
        coordinate: a string map coordinate

    Returns:
        the string coordinate split into its individual components.
    """
    return tuple(coordinate)


def compare_records(azara_record: Tuple, rui_record: Tuple) -> bool:
    """Compare two record types and determine if their coordinates match.

    Args:
        azara_record: a (treasure, coordinate) pair.
        rui_record:
            a (location, tuple(coordinate_1, coordinate_2), quadrant) trio.

    Returns:
        do the coordinates match?
    """
    return convert_coordinate(azara_record[1]) == rui_record[1]


def create_record(
    azara_record: Tuple, rui_record: Tuple
) -> Union[Tuple[str, str], Literal["not a match"]]:
    """Combine the two record types (if possible) and create a combined record.

    Args:
        azara_record: a (treasure, coordinate) pair.
        rui_record: a (location, coordinate, quadrant) trio.

    Returns:
        the combined record (if compatible),
        or the string "not a match" (if incompatible).
    """

    return (
        (*azara_record, *rui_record)
        if compare_records(azara_record, rui_record)
        else "not a match"
    )


def clean_up(combined_record_group: Tuple) -> str:
    """Create a combined record into a multi-line string of single records.

    Args:
        combined_record_group: everything from both participants.

    Returns:
        everything "cleaned", excess coordinates and information are removed.
    """
    report = ""

    for record in combined_record_group:
        report += str((*record[:1], *record[2:])) + "\n"

    return report
