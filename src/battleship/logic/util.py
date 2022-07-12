from battleship.logic.constants import VesselLength, column_mapping, row_mapping


def is_straight_line(coordinates):
    (start_column_idx, start_row_idx), (end_column_idx, end_row_idx) = coordinates

    if start_column_idx == end_column_idx or start_row_idx == end_row_idx:
        return True
    return False


def is_valid_length(coordinates, vessel_type):
    (start_column_idx, start_row_idx), (end_column_idx, end_row_idx) = coordinates

    print(
        "!!!!",
        column_mapping[start_column_idx],
        column_mapping[end_column_idx],
        abs(column_mapping[start_column_idx] - column_mapping[end_column_idx]),
        VesselLength[vessel_type.value].value - 1,
    )
    if start_column_idx == end_column_idx:
        print("GOT HERE")
        return abs(row_mapping[start_row_idx] - row_mapping[end_row_idx]) == VesselLength[vessel_type.value].value - 1
    elif start_row_idx == end_row_idx:
        print("IN HERE")
        return abs(column_mapping[start_column_idx] - column_mapping[end_column_idx]) == VesselLength[vessel_type.value].value - 1


def is_position_on_board(coordinates):
    (start_column_idx, start_row_idx), (end_column_idx, end_row_idx) = coordinates
    try:
        row_mapping[start_row_idx]
        row_mapping[end_row_idx]
        column_mapping[start_column_idx]
        column_mapping[end_column_idx]
        return True
    except KeyError as e:
        print("KeyError received", e)
        return False
