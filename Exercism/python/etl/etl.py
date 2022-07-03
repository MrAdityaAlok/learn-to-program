"""This module implement functions to tranform legacy data into new format."""

from collections import ChainMap
from typing import Dict


def transform(legacy_data: Dict) -> Dict:
    """Tranforms legacy data into new format.

    Args:
        legacy_data: Data to transform into new format.
    """
    return dict(
        ChainMap(
            *(
                dict.fromkeys(
                    map(lambda letter: letter.lower(), letters), score
                )
                for score, letters in legacy_data.items()
            )
        )
    )
