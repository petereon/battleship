import numpy as np

from battleship.logic.constants import GameStatus, Peg, column_mapping, row_mapping
from battleship.logic.player import Player


class Game:
    opponent: Player
    current_player: Player

    def __init__(self):
        self.player1 = Player()
        self.player2 = Player()
        self.current_player = self.player1
        self.opponent = self.player2
        self.status = None

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

    def check_sunk_vessel_status(self) -> bool:
        shot = self.current_player.get_current_shot()
        vessel_identifier = self.opponent.ocean_grid.matrix[shot[0]][shot[1]]

        vessel_holes = np.argwhere(self.opponent.ocean_grid.matrix == vessel_identifier)
        hit_holes = np.argwhere(self.current_player.target_grid.matrix == Peg.RED)

        for vessel_hole in vessel_holes:
            if not (hit_holes == vessel_hole).all(axis=1).any():
                return False
        return True

    def update_sunk_vessel_indicator(self):
        if self.check_sunk_vessel_status():
            list_of_pegs = self.current_player.sunk_vessel_indicator.tolist()
            list_of_pegs.pop()
            list_of_pegs = [Peg.RED] + list_of_pegs
            self.current_player.sunk_vessel_indicator = np.array(list_of_pegs)

    def take_turn(self, shot_hole: tuple):
        self.current_player.take_shot(shot_hole)
        self.place_peg(shot_hole)
        self.update_sunk_vessel_indicator()
        if (self.current_player.sunk_vessel_indicator == np.array([Peg.RED, Peg.RED, Peg.RED, Peg.RED, Peg.RED])).all():
            if self.current_player == self.player1:
                self.status = GameStatus.PLAYER_1_WON
            else:
                self.status = GameStatus.PLAYER_2_WON
        (self.current_player, self.opponent) = (self.opponent, self.current_player)
