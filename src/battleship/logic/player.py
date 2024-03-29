import numpy as np

from battleship.logic.constants import (
    Vessel,
    VesselIdentifier,
    column_mapping,
    row_mapping,
)
from battleship.logic.grid import Grid
from battleship.logic.util import is_valid_position_for_vessel


class PositionError(Exception):
    def __init__(self, message="Invalid position"):
        self.message = message
        super().__init__(self.message)


class Player:
    current_shot: tuple | None = None

    def __init__(self):
        self.ocean_grid = Grid()
        self.target_grid = Grid()
        self.sunk_vessel_indicator = np.zeros((5))

    def get_ship_coordinates(self, coordinates: tuple) -> tuple:
        start_column_idx = column_mapping[coordinates[0][0]]
        start_row_idx = row_mapping[coordinates[0][1]]
        end_column_idx = column_mapping[coordinates[1][0]]
        end_row_idx = row_mapping[coordinates[1][1]]
        return ((start_column_idx, start_row_idx), (end_column_idx, end_row_idx))

    def get_current_shot(self):
        if isinstance(self.current_shot, tuple) and len(self.current_shot) == 2:
            return self.current_shot
        raise Exception(f"Current shot is {self.current_shot}")

    def __place_valid_vessel(self, start_column_idx, end_column_idx, start_row_idx, end_row_idx, vessel_type):
        self.ocean_grid.matrix[start_column_idx][start_row_idx] = VesselIdentifier[vessel_type.value]
        if start_column_idx != end_column_idx:
            current_column_idx = start_column_idx
            while current_column_idx < end_column_idx:
                current_column_idx += 1
                self.ocean_grid.matrix[current_column_idx][start_row_idx] = VesselIdentifier[vessel_type.value]
        else:
            current_row_idx = start_row_idx
            while current_row_idx < end_row_idx:
                current_row_idx += 1
                self.ocean_grid.matrix[start_column_idx][current_row_idx] = VesselIdentifier[vessel_type.value]

    def place_vessel(self, vessel_type: Vessel, coordinates: tuple):
        try:
            if not is_valid_position_for_vessel(coordinates, vessel_type):
                raise PositionError()
            ((start_column_idx, start_row_idx), (end_column_idx, end_row_idx)) = self.get_ship_coordinates(coordinates)
            self.__place_valid_vessel(start_column_idx, end_column_idx, start_row_idx, end_row_idx, vessel_type)
        except PositionError:
            raise PositionError()

    def is_hole_available(self, hole: tuple) -> bool:
        column, row = (column_mapping[hole[0]], row_mapping[hole[1]])
        target_hole = self.target_grid.matrix[column][row]
        return bool(target_hole == 0)

    def take_shot(self, hole: tuple) -> None:
        self.current_shot = (column_mapping[hole[0]], row_mapping[hole[1]])

    def check_sunk_vessel_indicator(self):
        return self.sunk_vessel_indicator
