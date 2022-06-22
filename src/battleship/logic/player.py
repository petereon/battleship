from battleship.logic import Grid


class Player:
    def __init__(self):
        self.ocean_grid = Grid()
        self.target_grid = Grid()
