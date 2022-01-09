def saddle_points(matrix):
    points = []
    cached_column_mins = {}
    row_len = len(matrix[0]) if matrix else 0
    for i, row in enumerate(matrix):
        if len(row) != row_len:
            raise ValueError("Invalid matrix")
        _max = max(row)
        max_in_row = [_i for _i in range(row.index(_max), row_len) if row[_i] == _max]
        for m in max_in_row:
            if m not in cached_column_mins:
                cached_column_mins[m] = min(_row[m] for _row in matrix)
            if row[m] == cached_column_mins[m]:
                points.append({"row": i + 1, "column": m + 1})
    return points
