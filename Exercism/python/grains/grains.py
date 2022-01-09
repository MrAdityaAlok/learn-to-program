def square(number: int) -> int:
    if 1 < number > 64:
        raise ValueError(f"number should be between 1 and 64, was {number}")
    return 1 << (number - 1)  # 1 * 2^(number-1)


def total() -> int:
    return (1 << 64) - 1  # 2^64 -1 = 1.844674407371e+19
