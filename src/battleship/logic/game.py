from battleship.logic.constants import Peg, column_mapping, row_mapping
from battleship.logic.player import Player


class Game:
    opponent: Player
    current_player: Player

    def __init__(self):
        self.player1 = Player()
        self.player2 = Player()
        self.current_player = self.player1
        self.opponent = self.player2

    def check_shot_status(self, shot_hole: tuple) -> bool:
        column, row = (column_mapping[shot_hole[0]], row_mapping[shot_hole[1]])
        return bool(self.opponent.ocean_grid.matrix[column][row] != 0)

    def place_peg(self, hole: tuple):
        column, row = (column_mapping[hole[0]], row_mapping[hole[1]])
        if self.check_shot_status(hole):
            self.current_player.target_grid.matrix[column][row] = Peg.RED
        else:
            self.current_player.target_grid.matrix[column][row] = Peg.WHITE
