def is_straight_line(coordinates):
    (start_column_idx, start_row_idx), (end_column_idx, end_row_idx) = coordinates

    if start_column_idx == end_column_idx or start_row_idx == end_row_idx:
        return True
    return False
