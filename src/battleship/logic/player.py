from battleship.logic.grid import Grid


class Player:
    def __init__(self):
        self.ocean_grid = Grid()
        self.target_grid = Grid()
