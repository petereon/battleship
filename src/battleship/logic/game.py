import numpy as np

from battleship.logic.constants import (
    Peg,
    VesselIdentifier,
    column_mapping,
    row_mapping,
)
from battleship.logic.player import Player


class Game:
    opponent: Player
    current_player: Player

    def __init__(self):
        self.player1 = Player()
        self.player2 = Player()
        self.current_player = self.player1
        self.opponent = self.player2
        self.sunk_vessel_indicator = np.zeros((5))

    def check_shot_status(self, shot_hole: tuple) -> bool:
        column, row = (column_mapping[shot_hole[0]], row_mapping[shot_hole[1]])
        return bool(self.opponent.ocean_grid.matrix[column][row] != 0)

    def place_peg(self, hole: tuple):
        column, row = (column_mapping[hole[0]], row_mapping[hole[1]])
        self.opponent.ocean_grid.matrix[column][row] = Peg.RED
        if self.check_shot_status(hole):
            self.current_player.target_grid.matrix[column][row] = Peg.RED
        else:
            self.current_player.target_grid.matrix[column][row] = Peg.WHITE

    def check_sunk_vessel_status(self, shot_hole: tuple) -> bool:
        vessel_identifier = self.opponent.ocean_grid.matrix[column_mapping[shot_hole[0]]][row_mapping[shot_hole[1]]]

        vessel_holes = np.argwhere(self.opponent.ocean_grid.matrix == vessel_identifier)
        hit_holes = np.argwhere(self.current_player.target_grid.matrix == Peg.RED)

        for vessel_hole in vessel_holes:
            if not (hit_holes == vessel_hole).all(axis=1).any():
                return False
        return True

    def check_sunk_vessel_indicator(self):
        return self.sunk_vessel_indicator

    def update_sunk_vessel_indicator(self, shot_hole: tuple):
        if self.check_sunk_vessel_status(shot_hole):
            list_of_pegs = self.sunk_vessel_indicator.tolist()
            list_of_pegs.pop()
            list_of_pegs = [Peg.RED] + list_of_pegs
            self.sunk_vessel_indicator = np.array(list_of_pegs)
