from battleship.logic.constants import column_mapping, row_mapping
from battleship.logic.player import Player


class Game:
    opponent: Player

    def __init__(self):
        self.player1 = Player()
        self.player2 = Player()
        self.opponent = self.player2

    def check_shot_status(self, shot_hole: tuple) -> bool:
        column, row = (column_mapping[shot_hole[0]], row_mapping[shot_hole[1]])
        return bool(self.opponent.ocean_grid.matrix[column][row] != 0)
