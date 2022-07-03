"""This module defines function to transcribe dna strand into rna."""

from enum import Enum


class Complement(Enum):
    """Complements of dna nucelotide."""

    A = "U"
    T = "A"
    G = "C"
    C = "G"


def to_rna(dna_strand: str) -> str:
    """Convert dna sequence into rna."""
    return "".join(
        map(lambda nucelotide: Complement[nucelotide].value, dna_strand)
    )
