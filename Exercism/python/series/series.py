def slices(series, length):
    len_series = len(series)
    if length > len_series or length < 1:
        raise ValueError(
            f"Cannot get series of {length} digit/s out of just {len_series} digit/s number"
        )
    return [series[i : length + i] for i in range(len_series - length + 1)]
