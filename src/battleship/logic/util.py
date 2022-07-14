from battleship.logic.constants import VesselLength, column_mapping, row_mapping


def __is_straight_line(coordinates) -> bool:
    (start_column_idx, start_row_idx), (end_column_idx, end_row_idx) = coordinates

    result = False
    if start_column_idx == end_column_idx or start_row_idx == end_row_idx:
        result = True
    return result


def __is_valid_length(coordinates, vessel_type) -> bool:
    (start_column_idx, start_row_idx), (end_column_idx, end_row_idx) = coordinates

    result = False
    if start_column_idx == end_column_idx:
        result = abs(row_mapping[start_row_idx] - row_mapping[end_row_idx]) == VesselLength[vessel_type.value].value - 1
    elif start_row_idx == end_row_idx:
        result = abs(column_mapping[start_column_idx] - column_mapping[end_column_idx]) == VesselLength[vessel_type.value].value - 1

    return result


def __is_position_on_board(coordinates) -> bool:
    (start_column_idx, start_row_idx), (end_column_idx, end_row_idx) = coordinates
    try:
        row_mapping[start_row_idx]
        row_mapping[end_row_idx]
        column_mapping[start_column_idx]
        column_mapping[end_column_idx]
        return True
    except KeyError:
        return False


def is_valid_position_for_vessel(coordinates, vessel_type) -> bool:
    return __is_position_on_board(coordinates) and __is_valid_length(coordinates, vessel_type) and __is_straight_line(coordinates)
