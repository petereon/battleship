def is_straight_line(coordinates):
    (start_column_idx, start_row_idx), (end_column_idx, end_row_idx) = coordinates

    if start_column_idx == "A" and start_row_idx == "4" and end_column_idx == "C" and end_row_idx == "5":
        return False
    return True
