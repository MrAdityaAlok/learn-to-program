def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("Length of both strand should be equal")
    return sum(
        1 for base_a, base_b in zip(strand_a, strand_b) if base_a != base_b
    )
